from django.urls import path
from .views import *

urlpatterns=[
    path('', home, name="home"),
    path('channels/', user_channels, name='user_channels'),
    path('subjects/<int:channel_id>/', user_subjects, name='user_subjects'),
    path('chat',chat_view,name='chat'),
    path('chat/<username>', get_or_create_chatroom, name="start-chat"),
    path('chat/room/<chatroom_name>', chat_view, name="chatroom"),
    path('chat/new_groupchat/', create_groupchat, name="new-groupchat"),
    path('chat/edit/<chatroom_name>/',chatroom_edit_view, name="edit-chatroom"),
    path('chat/delete/<chatroom_name>/', chatroom_delete_view, name="chatroom-delete"),
    path('chat/leave/<chatroom_name>/', chatroom_leave_view, name="chatroom-leave"),
    path('chat/fileupload/<chatroom_name>/', chat_file_upload, name="chat-file-upload"),
    path('channel/<int:channel_id>/subject/<int:subject_id>/general/', subject_general, name="subject_general"),
    path('channel/<int:channel_id>/subject/<int:subject_id>/files/', subject_files, name="subject_files"),
    path('channel/<int:channel_id>/subject/<int:subject_id>/assignments/', view_assignment, name="view_assignment"),
    path('channel/<int:channel_id>/subject/<int:subject_id>/members/', view_members, name="view_members"),
    path('channel/<int:channel_id>/subject/<int:subject_id>/admins/', view_admins, name="view_admins"),
    path('channel/<int:channel_id>/subject/<int:subject_id>/assignments/create/', create_assignment, name="create_assignment"),
    path('assignments/<int:assignment_id>/submit/', submit_assignment, name="submit_assignment"),
    path('assignments/<int:assignment_id>/submissions/', view_submissions, name="view_submissions"),
    path("channel/<int:channel_id>/subject/<int:subject_id>/staff/", staff_view_assignments, name="staff_view_assignments"),
    path('assignment/<int:assignment_id>/close/', close_assignment, name='close_assignment'),
    path('assignment/<int:assignment_id>/allow-late/', allow_late_turn_in, name='allow_late_turn_in'),
    path('assignment/<int:assignment_id>/late-turn-in/', late_turn_in, name='late_turn_in'),

]

#path('chat/sendvoice/<chatroom_name>/', send_voice_note, name="send-voice-note"),


    
