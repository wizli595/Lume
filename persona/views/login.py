from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'persona/login.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile', username=request.user.username)
        return super().dispatch(request, *args, **kwargs)