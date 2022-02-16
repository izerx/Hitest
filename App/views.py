from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
import random, string
import json

def random_string(n):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(n))

@login_required(login_url='/accounts/login/')
def index(request):
    profile = request.user.profile
    if request.is_ajax():
        if request.POST.get('action') == "add_question":
            Subject.objects.get(id=request.POST.get('subject_id')).questions.add(Question.objects.create(
                text = request.POST.get('text'), right_answer = request.POST.get('answer'), 
                wrong_answers = str([request.POST.get('q_dop_1'), request.POST.get('q_dop_2'), request.POST.get('q_dop_3')])
            ))
        if request.POST.get('action') == "run_test":
            subject = Subject.objects.get(id=request.POST.get('subject_id'))
            test = Test.objects.create(date=date.today(), student=profile, subject=subject)
            test.questions.set(sorted(subject.questions.all(), key=lambda a: random.random())[0:5])
            test.save()
            return HttpResponse(json.dumps({'id': test.id}), content_type='application/json')
    context = {
       "Subjects": Subject.objects.all() if profile.status == 0 else Subject.objects.filter(teacher=profile)
    }
    return render(request, "App/index.html", context)

@login_required(login_url='/accounts/login/')
def history(request):
    profile = request.user.profile
    context = {
       "complete_tests": Result.objects.filter(student=profile) if profile.status == 0 else Result.objects.filter(subject__in = Subject.objects.filter(teacher=profile).all())
    }
    return render(request, "App/history.html", context)

@login_required(login_url='/accounts/login/')
def questions(request, id):
    profile = request.user.profile
    subject = Subject.objects.get(id=id)
    if request.is_ajax():
        if request.POST.get('action') == "add_question":
            subject.questions.add(Question.objects.create(
                text = request.POST.get('text'), right_answer = request.POST.get('answer'), 
                wrong_answers = str([request.POST.get('q_dop_1'), request.POST.get('q_dop_2'), request.POST.get('q_dop_3')])
            ))
            subject.save()
            template = loader.get_template('App/include/question.html')

            context = {
                "subject": subject
            }

            resp = template.render(context, request)
            return HttpResponse(resp)
    context = {
       "subject": subject
    }
    return render(request, "App/questions.html", context)

@login_required(login_url='/accounts/login/')
def test(request, id):
    profile = request.user.profile
    test = Test.objects.get(id=id)
    if test.student != profile or test.is_complete:
        return render(request, "App/access_denied.html")
    if request.is_ajax():
        if request.POST.get('action') == "complete_test":
            cnt_right, cnt_wrong = 0, 0
            answers = []
            for question in test.questions.all():
                answer = request.POST.get(f'group_answers_{question.id}')
                answers.append({"text":question.text,"right_answer": question.right_answer, "answer": answer})
                if question.right_answer == answer:
                    cnt_right+=1
                else:
                    cnt_wrong+=1
            test.is_complete = True
            test.save()
            res = Result.objects.create(date=test.date, student=profile, number_test=test.id, subject=test.subject, all_questions_count=test.questions.count(), right_answers=cnt_right, wrong_answers=cnt_wrong, answers=str(answers))
            return HttpResponse(json.dumps({'id': res.id}), content_type='application/json')
    context = {
        "test": test
    }
    return render(request, "App/test.html", context)

@login_required(login_url='/accounts/login/')
def result(request, id):
    test = Result.objects.get(id=id)
    if test.student != request.user.profile and request.user.profile.status == 0:
        return render(request, "App/access_denied.html")
    context = {
        "test": test
    }
    return render(request, "App/result.html", context)
