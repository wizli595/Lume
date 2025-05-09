from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = 'landing.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team"] = [
          {"initial": "Y", "name": "Youssef", "role": "Backend Specialist"},
          {"initial": "W", "name": "Wizli", "role": "Fullstack Engineer"},
          {"initial": "S", "name": "Salim", "role": "UI/UX Designer"},
          {"initial": "I", "name": "Ilias", "role": "Cloud Engineer"}
        ]
        context["features"] = [
            {"emoji": "📝", "title": "Articles", "desc": "Create and share articles with the world."},
            {"emoji": "🏷️", "title": "Tags", "desc": "Categorize and explore by topics and tags."},
            {"emoji": "💬", "title": "Comments", "desc": "Comment, react, and chat with the community."},
        ]
        return context
