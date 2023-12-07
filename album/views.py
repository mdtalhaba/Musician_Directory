from django.shortcuts import render, redirect
from album.forms import AlbumForm
from album.models import Album

def add_album(req) :
    if req.method == 'POST' :
        album_form = AlbumForm(req.POST)
        if album_form.is_valid() :
            album_form.save()
            return redirect('add_album')
    album_form = AlbumForm()
    return render(req, 'album/add_album.html', {'form' : album_form})


def edit_album(req, id) :
    album = Album.objects.get(pk=id)
    album_form = AlbumForm(instance=album)
    if req.method == 'POST' :
        album_form = AlbumForm(req.POST, instance=album)
        if album_form.is_valid() :
            album_form.save()
            return redirect('home')

    return render(req, 'album/add_album.html', {'form' : album_form})



