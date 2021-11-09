from django.shortcuts import render
from django.conf import settings
from . import business
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect


def show_all_polls(request):
    return render(request, str(settings.BASE_DIR) + "/templates/all_available_polls/index.html",
                  {'polls': business.get_all_polls()})


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
    business.save_poll(data)
    return redirect("/all_polls/")


def show_poll(request, id):
    return render(request, str(settings.BASE_DIR) + "/templates/poll_inspection/poll.html",
                  {'poll': business.get_poll_by_id(id)})


@api_view(["POST"])
def send_poll_answers(request):
    data = {
        "id": request.POST.get('id'),
        "questions": [
            {"question" + str(key): request.POST.get("question" + str(key))} for key in range(10)
        ]
    }

    question_answers = []
    for index in range(10):
        question_data = request.POST.get("question" + str(index))
        if question_data:
            question_answers.append({'question' + str(index): question_data})

    data['questions'] = question_answers
    business.save_answers(data)
    return Response("OK")
