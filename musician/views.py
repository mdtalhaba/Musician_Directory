from musician.forms import MusicianForm
from musician.models import Musician
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class AddMusicianView(CreateView) :
    model = Musician
    form_class = MusicianForm
    template_name = 'musician/add_musician.html'
    success_url = reverse_lazy('add_musician')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Musician Created Successfull')
        return super().form_valid(form)


@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class EditMusicianView(UpdateView) :
    model = Musician
    form_class = MusicianForm
    template_name = 'musician/add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.object.id
        context["id"] = id
        context["type"] = 'Edit'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Musician Updated Successfull')
        return super().form_valid(form)



@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class DeleteMusicianView(DeleteView) :
    model = Musician
    template_name = 'musician/delete_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

