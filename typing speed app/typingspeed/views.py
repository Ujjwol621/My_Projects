from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from typeaap.models import UserProfile
from django.shortcuts import render, redirect
from django.contrib import messages
import random
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about_us.html")
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
    
        if UserProfile.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username is already taken'})
        elif password1!=password2:
            return render(request, 'signup.html', {'error': 'password didnt matched'})
        else:
            myuser=UserProfile.objects.create_user(username,email,password1)
            myuser.first_name=request.POST['fname']
            # myuser.wpm=0
            # myuser.accuracy=0
            myuser.last_name=request.POST['lname']
            myuser.save()

            messages.success(request,"Your account has been successfully created!!!")
            return redirect('login')
    return render(request, 'signup.html')

def custom_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']

        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'login.html',{'error': "wrong credentials!!!!"})
    if messages.get_messages(request):
        for message in messages.get_messages(request):
            if message.tags == 'success':
                signup_success_message = message
                break
        else:
            signup_success_message = None
    else:
        signup_success_message = None
    return render(request, 'login.html', {'signup_success_message': signup_success_message})
def signout(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')

def start(request):
    file=open('new.txt', 'r')
    words = file.read().split()

    # Select 90 random words
    random.shuffle(words)
    paragraph = ' '.join(words[:90])

    context = {
        'paragraph': paragraph,
    }
    return render(request, 'start.html', context)

from django.utils import timezone
def result(request):
    # Calculate words per minute (WPM) and accuracy
    #start_time = timezone.now()
    #end_time = start_time + timezone.timedelta(seconds=30)  # Assuming 30-second limit

    typed_text = request.POST.get('typedText', '').split()
    original_text = request.POST.get('text', '').split()

    typed_words =0
    for i in range(0,len(typed_text)):
        if typed_text[i]==original_text[i]:
            typed_words +=1
    #time_elapsed = (end_time - start_time).total_seconds() / 60  # Convert seconds to minutes
    wpm = 2*typed_words

    accuracy = (typed_words/(len(typed_text)))*100
    if request.user.is_authenticated:
        profile= request.user
        current_wpm = profile.wpm
        current_accuracy = profile.accuracy
        if wpm>current_wpm:
            profile.wpm=wpm
            profile.accuracy=accuracy
        profile.save()

    context = {
        'wpm': round(wpm, 2),
        'accuracy': round(accuracy, 2)  # Convert accuracy to percentage
    }
    return render(request, 'result.html', context)

def leaderboard(request):
    # Retrieve user profiles and order them by WPM and accuracy
    user_profiles = UserProfile.objects.all().exclude(is_staff=True).order_by('-wpm', '-accuracy')

    # Pass the sorted user profiles to the template
    context = {'user_profiles': user_profiles}
    return render(request, 'leaderboard.html', context)
    