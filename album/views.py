from album.forms import AlbumForm
from album.models import Album
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class AddAlbumView(CreateView) :
    model = Album
    form_class = AlbumForm
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('add_album')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Album Created Successfull')
        return super().form_valid(form)


@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class EditAlbumView(UpdateView) :
    model = Album
    form_class = AlbumForm
    template_name = 'album/add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Edit'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Album Updated Successfull')
        return super().form_valid(form)
    

@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class DeleteAlbumView(DeleteView) :
    model = Album
    template_name = 'album/delete_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')



