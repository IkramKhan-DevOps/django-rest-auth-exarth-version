from django.views.generic import TemplateView
from django.urls import re_path
from .views import RegisterView, VerifyEmailView

urlpatterns = [
    re_path(r'^$', RegisterView.as_view(), name='rest_register'),
    re_path(r'^verify-email/$', VerifyEmailView.as_view(), name='rest_verify_email'),

    # This re_path is used by django-allauth and empty TemplateView is
    # defined just to allow reverse() call inside app, for example when email
    # with verification link is being sent, then it's required to render email
    # content.

    # account_confirm_email - You should override this view to handle it in
    # your API client somehow and then, send post to /verify-email/ endpoint
    # with proper key.
    # If you don't want to use API on that step, then just use ConfirmEmailView
    # view from:
    # django-allauth https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email'),
]
