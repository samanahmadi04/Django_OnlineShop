from django import forms
from .models import contactus
from django.core import validators


class contactUsFormModel(forms.ModelForm):
    class Meta:
        model = contactus
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['response']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message'
            })
        }
        labels = {  # نمیدونم چرا ولی لیبل ها کار نکرد
                     'full_name': 'اسم و فامیل',
                     'email': 'حساب الکتریکی',
                     'title': 'موضوع پیام',
                     'message': 'متن پیام شما'
                 },
        error_messages = {
            'full_name': {
                'required': 'فیلد اسم و فامیل باید پر شود'
            },
        }


# class ProfileForm(forms.Form):
#     user_image = forms.ImageField(
#         label = 'فایل خود را بارگزاری کنید',
#         widget=forms.FileInput(attrs={
#             'class' : 'form-control',
#             'placeholder' : 'this is a test'
#         })
#     )

# class contactUsForm(forms.Form):
#     full_name = forms.CharField(
#         label='نام و نام خانوادگی',
#         max_length=50,
#         error_messages={
#             'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
#             'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد',
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'نام و نام خانوادگی خود را قرار دهید'
#         })
#     )
#
#     email = forms.EmailField(label='ایمیل',
#                              widget=forms.EmailInput(
#                                  attrs={'class': 'form-control',
#                                         'placeholder': 'ایمیل خود را وارد کنید'
#
#                                         }))
#
#     subject = forms.CharField(label='عنوان',
#                               widget=forms.TextInput(
#                                   attrs={'class': 'form-control',
#                                          'placeholder': 'عنوان نظر شما'
#                                          }))
#
#     text = forms.CharField(
#         label='متن پیام',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'message',
#                 'placeholder': 'متن نظر شما'
#             }
#         )
#     )
