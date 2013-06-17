# Create your views here.
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from monty.forms import ImageGuestForm
from monty.models import Round, PrizeImages
from monty.utils import encode_answer, decode_answer, safe_reveal
import random


def step_one(request):

    if request.method == 'POST':
        form = ImageGuestForm(request.session['doors'], False)(request.POST)
        if form.is_valid():
            request.session['player'] = form.cleaned_data['player']
            guess = int(form.cleaned_data['guess'])
            reveal = safe_reveal(request.session['correct'], guess)
            request.session['reveal'] = reveal
            print guess, reveal, request.session['correct']
            if request.session['guess_1'] != 0:
                print 'used back-button'

            request.session['guess_1'] = int(form.cleaned_data['guess'])
            door = PrizeImages.objects.filter(image_type='lose').order_by('?')[0]
            request.session['doors'][reveal-1] = door

            return HttpResponseRedirect('/play/step_two.html')
    else:
        correct = random.choice([1, 2, 3])
        request.session['correct'] = correct
        request.session['guess_1'] = 0
        request.session['guess_2'] = 0
        doors = PrizeImages.objects.filter(image_type='door').order_by('?')
        request.session['doors'] = list(doors[:3])
        initial = {
            'player': request.session.get('player', None)
        }
        form = ImageGuestForm(request.session['doors'], False)(initial=initial)

    tdict = {
        'GuessForm': form,
        'doors': request.session['doors'],
    }

    return render(request, 'step_one.html', tdict)


def step_two(request):

    doors = request.session['doors']

    if request.method == 'POST':
        form = ImageGuestForm(request.session['doors'], True)(request.POST)
        if form.is_valid():
            guess = int(form.cleaned_data['guess'])
            obj = Round(player=form.cleaned_data['player'],
                        prize_loc=request.session['correct'],
                        first_guess=request.session['guess_1'],
                        second_guess=guess)
            obj.save()
            if guess == int(request.session['correct']):
                return HttpResponseRedirect('/play/you_win.html')
            else:
                return HttpResponseRedirect('/play/you_lose.html')
    else:
        initial = {
            'guess': request.session['guess_1'],
            'player': request.session.get('player', None)}
        form = ImageGuestForm(request.session['doors'], True)(initial=initial)

    tdict = {
        'GuessForm': form,
        'reveal': request.session['reveal'],
        'guess': request.session['guess_1']
    }

    return render(request, 'step_two.html', tdict)


def you_win(request):

    return render(request, 'you_win.html', {})


def you_lost(request):

    return render(request, 'you_lost.html', {})