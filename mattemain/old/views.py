from django.shortcuts import render, redirect
from random import randint
from .forms import AnswerForm
from django.http import HttpResponse
from .models import NumberModel


# Create your views here.
def index(request):
    form = AnswerForm()

    number_one = randint(0, 10)
    number_two = randint(0, 10)
    m = NumberModel(number_one=number_one, number_two=number_two, summa=(number_one + number_two))
    m.save()

    if request.method == 'POST':
        print('post')
        form = AnswerForm(request.POST)
        if form.is_valid():
            print('is valid')
            answer = form.cleaned_data["svaret"]
            summa = NumberModel.objects.latest('id').summa
            if int(answer) == int(summa):
                print('yes')
                return HttpResponse('correct')
            else:
                print('no')
                return HttpResponse('wrong')

    else:
        return render(request, template_name='startsidan.html', context={'one': number_one, 'two': number_two, "form": form})


def correct(request):
    return HttpResponse('Correct!')


def wrong(request):
    return HttpResponse('Wrong!!')

