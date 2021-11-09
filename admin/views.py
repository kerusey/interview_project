from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from . import buisness


def index(request):
    return render(request, str(settings.BASE_DIR) + '/templates/login_page/new_poll.html')


@api_view(["POST"])
def process_login_page(request):
    login, password = request.POST.get('login'), request.POST.get('password')
    validation = buisness.check_if_admin_valid(login, password)
    return HttpResponse(f"{validation}")
