from django.urls import path
from . import views


urlpatterns = [
    path("new_poll/", views.start_new_poll, name="open_form_to_create_poll"),
    path("submit_poll/", views.submit_poll, name="process_poll"),
    path("all_polls/", views.show_all_polls, name="show_all_polls"),
    path("poll<int:id>/", views.show_poll, name="displays_specific_poll"),
    path("send_answers/", views.send_poll_answers, name="answered_questions_going_to_back")
]
