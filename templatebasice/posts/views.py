from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return HttpResponse(f"Welcome to the forum apps!")


def dashboard(request):
    if request.method == "POST":
        return redirect('index')
    context = {
        'posts': [
            {
                'title': 'How work with the templates?',
                'author': 'Dian Kalaydjiev',
                'content': '**Hey** how i *work* `with` the templates in Django',
                'created_at': datetime.now(),
                },
            {
                'title': 'Was Dido lecture goog?',
                'author': 'Anonymous',
                'content': 'Should I watched it',
                'created_at': datetime.now(),
            },
            {
                'title': 'what is the next lecture?',
                'author': '',
                'content': 'Hey guys i have no idea, pls answer',
                'created_at': datetime.now(),
            }
        ]
    }
    # context = {
    #     'first_name': 'Dian',
    #     'last_name': 'Kalaydjiev',
    #     'is_hungry': None,
    #     'favourite_songs': ['The ringer', 'Fall'],
    #     'current_time': datetime.now(),
    # }
    return render(request, 'base.html', context)