from django.shortcuts import render
from django.conf import settings
from . import buisness
from rest_framework.response import Response
from rest_framework.decorators import api_view


def show_all_polls(request):
    return render(request, str(settings.BASE_DIR) + "/templates/all_available_polls/index.html",
                 {'polls': buisness.get_all_polls()})


def start_new_poll(request):
    return render(request, str(settings.BASE_DIR) + "/templates/new_poll/new_poll.html")


@api_view(["POST"])
def submit_poll(request):
    data = {
        "name": request.POST.get('name'), "topic": request.POST.get('topic'),
        "description": request.POST.get('description'),
        "questions": [
            {"question" + str(key): request.POST.get("question" + str(key))} for key in range(10)
        ]
    }
    buisness.save_poll(data)
    return Response(buisness.get_all_polls())
