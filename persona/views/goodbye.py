from django.views.generic import TemplateView

class GoodbyeView(TemplateView):
    template_name = 'persona/goodbye.html'
