from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ..models import CustomUser
from pulse.models import Follow
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import UserProfile
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from persona.models import UserProfile
from django.http import HttpResponse
from django.template.loader import render_to_string

from django.shortcuts import redirect
class ProfileView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = CustomUser
    template_name = 'account/profile.html'
    slug_field = 'username'      
    slug_url_kwarg = 'username'   
    context_object_name = 'profile_user'
    login_url = 'login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = self.get_object()
        user = self.request.user

        context['is_admin_viewing']= user.is_superuser

        if user.is_authenticated and user != profile_user:
            context['is_following'] = Follow.objects.filter(follower=user, following=profile_user).exists()
        else:
            context['is_following'] = None  # or False

        return context
    def test_func(self):
        # Allow access only if the user is viewing their own profile
        # return self.request.user.username == self.kwargs['username']
        return True

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['avatar', 'bio']
    template_name = 'account/profile_edit.html'

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        form.save()
        if self.request.headers.get("HX-Request"):
            html = render_to_string("account/partials/profile_card.html", {
                "profile_user": self.request.user,
                "request": self.request,
                "is_following": None  # or recalculate if needed
            })
            return HttpResponse(html)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user.username})