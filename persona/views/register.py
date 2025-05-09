from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from ..forms import CustomUserCreationForm
from ..models import CustomUser
from django.shortcuts import redirect

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'persona/register.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    def get_success_url(self):
        return reverse_lazy('profile',kwargs={'username': self.object.username})  


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile', username=request.user.username)
        return super().dispatch(request, *args, **kwargs)  