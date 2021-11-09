from __future__ import annotations
import datetime
import pytz
from django.conf import settings
import json
import redis
from django.core.management.commands import flush

redis_instance = redis.Redis(host=settings.REDIS_HOST,
                             port=settings.REDIS_PORT, db=0)

redis_instance.flushdb()


def save_poll(data: dict) -> None:
    remove_from_list = []
    for index in range(len(data['questions'])):
        for key, value in data['questions'][index].items():
            if value is None:
                remove_from_list.append(index)

    questions = {}
    for counter in range(len(data['questions'])):
        if counter not in remove_from_list:
            key = list(data['questions'][counter].keys())[0]
            questions[key] = data['questions'][counter][key]

    data['questions'] = questions
    data['date_posted'] = str(datetime.datetime.now(pytz.timezone('Europe/Moscow')))
    data['date_expires'] = str(datetime.datetime.now(pytz.timezone('Europe/Moscow')) + datetime.timedelta(days=7))

    if redis_instance.get('current_id') is None:
        redis_instance.set('current_id', 1)
        redis_instance.set('poll_1', json.dumps(data))
    else:
        current_id = int(redis_instance.get('current_id').decode('utf-8'))
        redis_instance.set('current_id', current_id + 1)
        redis_instance.set(f'poll_{current_id}', json.dumps(data))


def get_poll_by_id(poll_id: int) -> dict | None:
    poll = redis_instance.get("poll_" + str(poll_id))
    if poll is None:
        return None
    requested_poll = json.loads(poll.decode("utf-8"))
    return requested_poll


def get_all_polls() -> dict:
    all_polls = {}
    id = 1
    while True:
        current_poll = get_poll_by_id(id)
        if current_poll is not None:
            all_polls[f'poll_{id}'] = current_poll
            id += 1
        else:
            return all_polls

