from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        assert request.user.is_authenticated
        url = reverse('profile', kwargs={'username': request.user.username})
        return url
