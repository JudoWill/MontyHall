# Create your views here.
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from monty.forms import GuessForm, ImageGuestForm
from monty.models import Round, PrizeImages
from monty.utils import encode_answer, decode_answer, safe_reveal
import random


def step_one(request):

    if request.method == 'POST':
        form = ImageGuestForm(request.session['doors'])
        if form.is_valid():
            print request.session['guess_1']
            reveal = safe_reveal(request.session['correct'], form.cleaned_data['guess'])
            print request.session['correct'], form.cleaned_data['guess'], reveal
            if request.session['guess_1'] != 0:
                print 'used back-button'
            else:
                request.session['guess_1'] = int(form.cleaned_data['guess'])

            return HttpResponseRedirect('/play/step_two.html')
    else:
        correct = random.choice([1, 2, 3])
        request.session['correct'] = correct
        request.session['guess_1'] = 0
        request.session['guess_2'] = 0
        doors = PrizeImages.objects.filter(image_type='door').order_by('?')
        request.session['doors'] = list(doors[:3])
        form = ImageGuestForm(request.session['doors'])

    tdict = {
        'GuessForm': form,
        'doors': request.session['doors'],
    }

    return render(request, 'step_one.html', tdict)


def step_two(request):

    if request.method == 'POST':
        form = GuessForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = GuessForm()

    return render(request, 'step_two.html', {'GuessForm': form})


def you_win(request):

    return render(request, 'you_win.html', {})


def you_lost(request):

    return render(request, 'you_lost.html', {})