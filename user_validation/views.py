from user_validation.forms import RegistrationForm, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
    

# User Register Using Class View
class UserRegisterView(CreateView) :
    model = User
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Registration Successfull')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Register'
        return context


# User Login Using Class View
class UserLoginView(LoginView) :
    template_name = 'register.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Log In Successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Log In Information is Incorrenct')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Log In'
        return context
    

# User Logout Using Class View
@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class UserLogoutView(LogoutView) :    
    def get_success_url(self):
        return reverse_lazy('login')
