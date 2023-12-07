from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import Musician

def add_musician(req) :
    if req.method == 'POST' :
        musician_form = MusicianForm(req.POST)
        if musician_form.is_valid() :
            musician_form.save()
            return redirect('add_musician')

    musician_form = MusicianForm()
    return render(req, 'musician/add_musician.html', {'form' : musician_form})


def edit_musician(req, id) :
    musician = Musician.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    if req.method == 'POST' :
        musician_form = MusicianForm(req.POST, instance=musician)
        if musician_form.is_valid() :
            musician_form.save()
            return redirect('home')

    return render(req, 'musician/add_musician.html', {'form' : musician_form})


def delete_musician(req, id) :
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')

