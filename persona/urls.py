from django.urls import path
from .views.goodbye import GoodbyeView
from .views.landing import LandingPageView
from .views.profile import ProfileView, ProfileUpdateView
from .views.peopleList import PeopleListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', LandingPageView.as_view(), name='landing'),
    path('goodbye/', GoodbyeView.as_view(), name='goodbye'),
    path('people/', PeopleListView.as_view(), name='people'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)