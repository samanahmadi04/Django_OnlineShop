from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us_view.as_view(), name='contact_us_page'),
    path('profile', views.CreateProfileView.as_view(), name='create_profile'),
    path('profiles', views.ProfileListView.as_view(), name='profiles')
]
