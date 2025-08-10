from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body':forms.TextInput(attrs={'placeholder': 'Add message ...', 'class': 'p-4 text-black', 'max_length': '300', 'autofocus': True}),
        }

class NewGroupForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name' : forms.TextInput(attrs={
                'placeholder' : 'Add name...',
                'class' : 'p-4 text-black',
                'max_length' : '300',
                'autofocus' : True,
            }),
        }
class ChatRoomEditForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name' : forms.TextInput(attrs={
                'class':'p-4 text-xl font-bold mb-4',
                'max_lenght':'300',
            }),
        }

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your post here...'}), required=True)
    
    class Meta:
        model = Post
        fields = ['body']

class FileUploadForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description of the file...'}), required=False)

    class Meta:
        model = File
        fields = ['file', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'file', 'due_date']
        widgets = {
                    'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                }

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['file']