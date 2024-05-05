from django.shortcuts import render, redirect
from random import randint
from .forms import AnswerForm
from django.http import HttpResponse
from .models import NumberModel
import time
from django.core.exceptions import ValidationError


def index(request):
    form = AnswerForm()

    # try:
    #     data = NumberModel.object.first()
    # except AttributeError:
    #     for x in range(1000):
    #         number_one = randint(0, 10)
    #         number_two = randint(0, 10)
    #         summa = number_one + number_two
    #         m = NumberModel(number_one=number_one, number_two=number_two, summa=summa)
    #         m.save()

    totalt_svarat = NumberModel.objects.filter(svarat=True).count()
    totalt_correct = NumberModel.objects.filter(svarat=True).filter(correct=True).count()

    data = NumberModel.objects.filter(svarat=False).first()
    number_one = data.number_one
    number_two = data.number_two

    if request.method == 'POST':
        print('post')
        form = AnswerForm(request.POST)
        if form.is_valid():
            print('is valid')
            answer = form.cleaned_data["svaret"]
            data = NumberModel.objects.filter(svarat=False).first()
            summa = data.summa
            print('answer: ', answer, 'summa: ', summa)
            if int(answer) == int(summa):
                print('yes')
                NumberModel.objects.filter(id=data.id).update(svarat=True, correct=True)
                return redirect('correct')
            else:
                print('no')
                NumberModel.objects.filter(id=data.id).update(svarat=True, correct=False)
                return redirect('wrong')

    else:
        return render(request, template_name='startsidan.html',
                      context={'one': number_one, 'two': number_two, "form": form,
                               "tot_svar": totalt_svarat, "tot_corr": totalt_correct})


def correct(request):

    return render(request, template_name="correct.html")


def wrong(request):

    return render(request, template_name="wrong.html")


def re_start(request):

    NumberModel.objects.update(svarat=False, correct=False)

    return render(request, template_name='re_start.html')
