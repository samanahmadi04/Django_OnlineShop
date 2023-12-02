from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from .forms import contactUsFormModel
from .models import contactus, UserProfile
# Create your views here.
from django.urls import reverse


# generic class bsae view that i have learned : View-TemplateView-FormView-CreateView-ListView-DetailView-


class contact_us_view(CreateView):
    template_name = 'contact_us/contact_us.html'
    form_class = contactUsFormModel
    success_url = 'contact_us'


class CreateProfileView(CreateView):
    template_name = 'contact_us/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact_us/'


class ProfileListView(ListView):
    model = UserProfile
    template_name = 'contact_us/profiles_list_page.html'
    context_object_name = 'ProFile'




# def store_profile(file):
#     with open('temp/image.jpg', "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, 'contact_us/create_profile_page.html', {
#             'form': form
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#
#         if submitted_form.is_valid():
#             # store_file(request.FILES['profile'])
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return redirect('/contact_us/profile')
#
#         return render(request, 'contact_us/create_profile_page.html', {
#             'form': submitted_form
#         })
