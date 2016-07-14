from django.contrib import admin
from django.conf.urls import url

from .views import (
    member_form,

)

urlpatterns = [
    url(r'^$',member_form)
]