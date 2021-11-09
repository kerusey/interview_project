from django.urls import path
from . import views


urlpatterns = [
    path("new_poll/", views.start_new_poll, name="show_all_polls"),
    path("submit_poll/", views.submit_poll, name="process_poll")
]
