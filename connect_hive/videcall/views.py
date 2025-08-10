from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def videocall(request):
    return render(request, 'videcall/videocall.html', {'name':request.user.username})
