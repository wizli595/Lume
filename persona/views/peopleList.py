from django.contrib.auth import get_user_model
from pulse.models import Follow
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class PeopleListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'account/people.html'
    context_object_name = 'people'

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        followed_ids = user.following.values_list('following_id', flat=True)
        context['followed_ids'] = set(followed_ids)
        return context
