from django.shortcuts import render
from .models import Superheroes
from .forms import MusicianForm, SuperheroForm

from .models import Musician
# Create your views here.
def showhome(request):
    return render(request, 'layouts/base.html', context={'primelist': None})


def showcon(request):
    form = MusicianForm()
    form1 = SuperheroForm()
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        form1 = SuperheroForm(request.POST)

        if form1.is_valid():
            print('form submitted')
            data=form1.cleaned_data
            #musician = Musician(data)
            form1.save()
        elif form.is_valid():
            print('form submitted')
            data=form.cleaned_data
            form.save()
        else:
            print('error')
    context = {'mu_form': form,'super_form':form1}
    return render(request, 'Contact.html', context=context)


def shownews(request):
    news = [{'title': 'Some title',
             'subtitle': ' Some subtitle',
             'description': 'once upon a time,there was a pizza',
             'link1': 'http://www.wikipedia.com',
             'link 2': 'http://www.polygon.com'
             },
            {'title': 'Some title 2',
             'subtitle': ' Some subtitle 2',
             'description': 'the  pizza gone',
             'link1': 'http://www.wikipedia.com',
             'link 2': 'http://www.polygon.com'
             }
            ]
    return render(request, 'layouts/news.html', context={'news': news})


def index(request):
    heroes = Superheroes.objects.all()  # select* from all superheroes  (query)
    context = {'heroes': heroes}
    return render(request, 'home.html', context)
