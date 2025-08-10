from django.db import models
from django.contrib.auth.models import User
import shortuuid
import os

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128,unique=True, default=shortuuid.uuid)
    groupchat_name = models.CharField(max_length=128, null=True, blank=True)
    admin = models.ForeignKey(User, related_name='groupchats', blank=True, null=True, on_delete=models.SET_NULL)
    user_online = models.ManyToManyField(User,related_name='online_in_groups',blank=True)
    members = models.ManyToManyField(User,related_name='chat_groups',blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name
    
class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    #audio_note = models.FileField(upload_to='voice_notes/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    file = models.FileField(upload_to='files/',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def filename(self):
        if self.file:
            return os.path.basename(self.file.name)
        else:
            return None
        
    def __str__(self):
        if self.body:
            return f'{self.author.username} : {self.body}'
        elif self.file:
            return f'{self.author.username} : {self.filename}'
    class Meta: 
        ordering = ['-created']

    @property
    def is_image(self):
        if self.filename.lower().endswith(('.jpg','.jpeg','.png','.gif','.svg','.webp')):
            return True
        else:
            return False

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, related_name="channels")  # Multiple subjects per channel
    members = models.ManyToManyField(User, related_name="channels")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_channels")

    def __str__(self):
        return self.name


class Post(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="posts")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField(blank=True)
    file = models.FileField(upload_to='shared_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_assignment_post = models.BooleanField(default=False)  # New field to flag assignment posts
    assignment = models.ForeignKey('Assignment', null=True, blank=True, on_delete=models.SET_NULL, related_name="posts")  # Link to the assignment if applicable


    # Thread replies
    parent_post = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")

    def __str__(self):
        return f"{self.author.username} in {self.channel.name} ({self.subject.name}) - {self.body[:30]}"

    class Meta:
        ordering = ['-created_at']



class File(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="files")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="files")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_files")
    file = models.FileField(upload_to='subject_files/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} uploaded by {self.uploaded_by.username} in {self.channel.name} ({self.subject.name})"

    @property
    def filename(self):
        return os.path.basename(self.file.name)

class Assignment(models.Model):
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="assignments")
    channel = models.ForeignKey("Channel", on_delete=models.CASCADE, related_name="assignments")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_assignments")  # Staff
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="assignments/", blank=True, null=True)  # Optional assignment file
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)  # New field
    allow_late_turn_in = models.BooleanField(default=False)  # Ensure this field exists
    def __str__(self):
        return f"Assignment: {self.title} by {self.created_by.username}"


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignment_submissions")  # Students
    file = models.FileField(upload_to="assignment_submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.submitted_by.username} for {self.assignment.title}"
