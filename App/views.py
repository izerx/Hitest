from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
import random, string

def random_string(n):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(n))

@login_required(login_url='/accounts/login/')
def index(request):
    student = request.user.student

    # for i in range(10):
    #     question = Question.objects.create(text=random_string(50),
    #     right_answer=random_string(20), wrong_answers=f'({random_string(20)}),({random_string(20)}),({random_string(20)})')
    try:
        test = Test.objects.get(date=date.today(), student=student)
    except Exception:
        test = Test.objects.create(date=date.today(), student=student)
        test.questions.set(Question.objects.order_by('?')[0:5])
        # ids = sorted([q.id for q in Question.objects.all()], key=lambda A: random.random())[0:5]
        # for id in ids:
        #     test.questions.add(Question.objects.get(id=id))
    print(Question.objects.order_by('?'))
    context = {
        "test": test
    }
    return render(request, "App/index.html", context)

@login_required(login_url='/accounts/login/')
def result(request, id):
    pass
