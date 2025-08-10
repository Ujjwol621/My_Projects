from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404
from django.utils import timezone
from .models import *
from .forms import *
@login_required
def home(request):
    return render(request,'home.html')
@login_required
def chat_view(request, chatroom_name='public-chat'):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()

    other_user = None
    if chat_group.is_private:
        if request.user not in chat_group.members.all():
            raise Http404()
        for member in chat_group.members.all():
            if member != request.user:
                other_user = member
                break
    if chat_group.groupchat_name:
        if request.user not in chat_group.members.all():
            if request.user.emailaddress_set.filter(verified=True).exists():
                chat_group.members.add(request.user)
            else:
                messages.warning(request, 'You need to verify you email to join the chat!')
                return redirect('profile-settings')

    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message' : message,
                'user' : request.user
            }
            return render(request, 'a_rtchat/partials/chat_message_p.html', context)

    context = {
        'chat_messages' : chat_messages, 
        'form' : form,
        'other_user' : other_user,
        'chatroom_name' : chatroom_name,
        'chat_group' : chat_group
    }
    return render(request, 'a_rtchat/chat.html',context)

@login_required
def get_or_create_chatroom(request, username):
    if request.user.username == username:
        return redirect('home')
    
    other_user = User.objects.get(username=username)
    my_chatrooms = request.user.chat_groups.filter(is_private = True)

    if my_chatrooms.exists():
        for chatroom in my_chatrooms:
            if other_user in chatroom.members.all():
                chatroom = chatroom
                break
            else:
                chatroom = ChatGroup.objects.create(is_private = True)
                chatroom.members.add(other_user,request.user)
    else:
        chatroom = ChatGroup.objects.create(is_private=True)
        chatroom.members.add(other_user, request.user)

    return redirect('chatroom', chatroom.group_name)

@login_required
def create_groupchat(request):
    form = NewGroupForm()
    if request.method == 'POST':
        form = NewGroupForm(request.POST)
        if form.is_valid():
            new_groupchat = form.save(commit=False)
            new_groupchat.admin = request.user
            new_groupchat.save()
            new_groupchat.members.add(request.user)
            return redirect('chatroom', new_groupchat.group_name )

    context = {
        'form' : form
    }
    return render(request, 'a_rtchat/create_groupchat.html',context)

@login_required
def chatroom_edit_view(request, chatroom_name):
    chat_group = get_object_or_404(ChatGroup,group_name=chatroom_name)
    if request.user != chat_group.admin:
        raise Http404()
    
    form =ChatRoomEditForm(instance=chat_group)

    if request.method == 'POST':
        form =ChatRoomEditForm(request.POST, instance=chat_group)
        if form.is_valid():
            form.save()

            remove_members = request.POST.getlist('remove_members')
            for member_id in remove_members:
                member = User.objects.get(id=member_id)
                chat_group.members.remove(member)
            messages.success(request, 'Chatroom Updated Sucessfully!')
            return redirect('chatroom', chatroom_name)

    context = {
        'form':form,
        'chat_group' : chat_group
    }   
    return render(request,'a_rtchat/chatroom_edit.html',context)

@login_required
def chatroom_delete_view(request, chatroom_name):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    if request.user != chat_group.admin:
        raise Http404()
    
    if request.method == "POST":
        chat_group.delete()
        messages.success(request,'Chatroom Deleted!')
        return redirect('home')
    
    return render(request, 'a_rtchat/chatroom_delete.html',{'chat_group':chat_group})

@login_required
def chatroom_leave_view(request, chatroom_name):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    if request.user not in chat_group.members.all():
        raise Http404()

    if request.method == "POST":
        chat_group.members.remove(request.user)
        messages.success(request, 'You left the chat!')
        return redirect('home')
    
def chat_file_upload(request, chatroom_name):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)

    if request.htmx and request.FILES:
        file = request.FILES['file']
        message = GroupMessage.objects.create(
            file = file,
            author = request.user,
            group = chat_group,
        )
        channel_layer = get_channel_layer()
        event = {
            'type' : 'message_handler',
            'message_id' : message.id,
        }
        async_to_sync(channel_layer.group_send)(
            chatroom_name, event
        )
    return HttpResponse()

@login_required
def user_channels(request):
    user = request.user

    # Fetch channels where the user is a member
    channels = Channel.objects.filter(members=user)

    # If no associated channels, redirect to an error page or a default dashboard
    if not channels.exists():
        return render(request, "channel.html", {"user": user})

    # Render the channels page with the filtered list
    return render(request, "channel.html", {"channels": channels, "user": user})

@login_required
def user_subjects(request, channel_id):
    user = request.user

    # Get the channel for which subjects should be displayed
    channel = get_object_or_404(Channel, id=channel_id, members=user)

    # Get the subjects associated with this channel
    subjects = channel.subjects.all()

    return render(request, 'subjects.html', {'subjects': subjects, 'channel': channel, 'user': user})

@login_required
def subject_general(request, channel_id, subject_id):
    channel = get_object_or_404(Channel, id=channel_id, members=request.user)
    subject = get_object_or_404(Subject, id=subject_id, channels=channel)

    # Handle new post submission
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.subject = subject
            post.channel = channel
            post.save()
            return redirect("subject_general", channel_id=channel.id, subject_id=subject.id)
    else:
        form = PostForm()

    # Fetch posts for the specific subject in the channel
    posts = Post.objects.filter(channel=channel, subject=subject, parent_post__isnull=True).select_related("author")

    return render(request, "subject_general.html", {"channel": channel, "subject": subject, "posts": posts, "form": form})

@login_required
def subject_files(request, channel_id, subject_id):
    channel = get_object_or_404(Channel, id=channel_id, members=request.user)
    subject = get_object_or_404(Subject, id=subject_id, channels=channel)

    # Handle file upload
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.uploaded_by = request.user
            file_instance.subject = subject
            file_instance.channel = channel
            file_instance.save()
            return redirect("subject_files", channel_id=channel.id, subject_id=subject.id)
    else:
        form = FileUploadForm()

    # Fetch files for the specific subject in the channel
    files = File.objects.filter(channel=channel, subject=subject)

    return render(request, "subject_files.html", {"channel": channel, "subject": subject, "files": files, "form": form})

@login_required
def view_assignment(request, channel_id, subject_id):
    channel = get_object_or_404(Channel, id=channel_id, members=request.user)
    subject = get_object_or_404(Subject, id=subject_id, channels=channel)
    assignments = Assignment.objects.filter(subject=subject)
    now = timezone.now()

    
    # Get all submissions for this user related to these assignments
    submissions = AssignmentSubmission.objects.filter(
        submitted_by=request.user,
        assignment__in=assignments
    )
    
    # Create a list of assignment_ids that the user has already submitted
    submitted_assignment_ids = submissions.values_list("assignment_id", flat=True)

    # Filter assignments to show only those that are not yet submitted by the user
    unsubmitted_assignments = assignments.exclude(id__in=submitted_assignment_ids)

    return render(request, "view_assignment.html", {
        "channel":channel,
        "subject": subject,
        "assignments": unsubmitted_assignments,
        "submitted_assignment_ids": submitted_assignment_ids,
        "now": now,
    })

@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    subject = assignment.subject
    channel = assignment.channel

    # If it's a POST request, process the submitted file
    if request.method == "POST" and request.FILES.get("file"):
        # Create a new submission or update existing one
        submission, created = AssignmentSubmission.objects.update_or_create(
            assignment=assignment,
            submitted_by=request.user,
            defaults={"file": request.FILES["file"]},
        )

        # Redirect after successful submission
        messages.success(request, 'Assignment Submitted Sucessfully!')
        return redirect("view_assignment", channel_id=channel.id, subject_id=subject.id)

    # Render the submission form
    return render(request, "submit_assignment.html", {"assignment": assignment,"channel":channel,
        "subject": subject,})

@login_required
def staff_view_assignments(request, channel_id, subject_id):
    # Get the channel and subject
    channel = get_object_or_404(Channel, id=channel_id, members=request.user)
    subject = get_object_or_404(Subject, id=subject_id, channels=channel)
    now = timezone.now()

    # Get all assignments related to the subject and channel
    assignments = Assignment.objects.filter(subject=subject, channel=channel, closed=False)

    # Get all submissions related to the assignments
    submissions = AssignmentSubmission.objects.filter(assignment__in=assignments)
    submission_dict = {submission.assignment_id: submission for submission in submissions}

    return render(request, "staff_view_assignments.html", {
        "channel": channel,
        "subject": subject,
        "assignments": assignments,
        "submission_dict": submission_dict,
        "now":now,
    })

@login_required
def view_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    channel = assignment.channel
    subject = assignment.subject

    # Check if the user is staff and the assignment creator
    if not request.user.is_staff or assignment.created_by != request.user:
        return redirect("view_assignments", channel_id=assignment.channel.id, subject_id=assignment.subject.id)

    # Fetch all submissions for this assignment
    submissions = AssignmentSubmission.objects.filter(assignment=assignment)

    # Build a dictionary of submission details
    submission_dict = {
        submission.id: {
            "submitted_by": submission.submitted_by.username,
            "submitted_at": submission.submitted_at,
            "file_url": submission.file.url if submission.file else None,
        }
        for submission in submissions
    }

    # Pass submission_dict to the template
    return render(request, "view_submissions.html", {
        "assignment": assignment,
        "submission_dict": submission_dict,
        "channel":channel,
        "subject":subject,
    })

@login_required
def create_assignment(request, channel_id, subject_id):
    if not request.user.is_staff:
        return redirect("view_assignments", channel_id=channel_id, subject_id=subject_id)

    channel = get_object_or_404(Channel, id=channel_id, members=request.user)
    subject = get_object_or_404(Subject, id=subject_id, channels=channel)

    if request.method == "POST":
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the assignment
            assignment = form.save(commit=False)
            assignment.created_by = request.user
            assignment.channel = channel
            assignment.subject = subject
            assignment.save()

            # Create a post in the General section about the new assignment
            post = Post(
                channel=channel,
                subject=subject,
                author=request.user,
                body=f"New assignment created: {assignment.title}. Due Date: {assignment.due_date}.",
                is_assignment_post=True,  # Mark as an assignment post
                assignment=assignment,  # Link to the assignment
            )
            post.save()

            return redirect("staff_view_assignments", channel_id=channel_id, subject_id=subject_id)
    else:
        form = AssignmentForm()

    return render(request, "create_assignment.html", {"form": form, "channel": channel, "subject": subject})

def view_members(request, channel_id, subject_id):
    # Fetch the channel and subject objects
    channel = get_object_or_404(Channel, id=channel_id)
    subject = get_object_or_404(Subject, id=subject_id)
    
    # Retrieve all users related to this channel or subject
    # Adjust the query to match your user-channel/subject relationship
    members = User.objects.filter(is_staff=False, is_superuser=False)    
    context = {
        'channel': channel,
        'subject': subject,
        'members': members,
    }
    return render(request, 'view_members.html', context)

def view_admins(request, channel_id, subject_id):
    # Fetch the channel and subject objects
    channel = get_object_or_404(Channel, id=channel_id)
    subject = get_object_or_404(Subject, id=subject_id)
    
    # Retrieve all admins (staff users or superusers)
    admins = User.objects.filter(is_staff=True) | User.objects.filter(is_superuser=True)
    
    context = {
        'channel': channel,
        'subject': subject,
        'admins': admins,
    }
    return render(request, 'view_admins.html', context)

def close_assignment(request, assignment_id):
    if request.user.is_staff:
        assignment = get_object_or_404(Assignment, id=assignment_id)
        assignment.closed = True
        assignment.allow_late_turn_in = False  # Disable late submissions
        assignment.save()
        messages.success(request, "Assignment has been closed.")
    return redirect('staff_view_assignments', assignment.channel.id, assignment.subject.id)

def allow_late_turn_in(request, assignment_id):
    if request.user.is_staff:
        assignment = get_object_or_404(Assignment, id=assignment_id)
        assignment.closed = False
        assignment.allow_late_turn_in = True  # Allow late turn-in
        assignment.save()
        messages.success(request, "Late submissions are now allowed.")
    return redirect('staff_view_assignments', assignment.channel.id, assignment.subject.id)


def late_turn_in(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    subject = assignment.subject
    channel = assignment.channel
    if request.method == "POST" and request.FILES.get("file") and not assignment.closed:
    # Create a new submission or update existing one
        submission, created = AssignmentSubmission.objects.update_or_create(
        assignment=assignment,
        submitted_by=request.user,
        defaults={"file": request.FILES["file"]},
    )
        # Logic for submitting the assignment
        messages.success(request, "Assignment submitted late.")
        return redirect("view_assignment", channel_id=channel.id, subject_id=subject.id)

    # Render the submission form
    return render(request, "submit_assignment.html", {"assignment": assignment,"channel":channel,
        "subject": subject,})
