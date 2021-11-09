from django.urls import path
from . import views


urlpatterns = [
	path("admin/", views.index, name="admin_login"),
	path("login/", views.process_login_page, name="authentification_login"),
]
