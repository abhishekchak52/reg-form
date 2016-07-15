from django.conf.urls import url

from .views import (
    member_form,
    member_success,

)

urlpatterns = [
    url(r'^$', member_form),
    url(r'^success/$', member_success, name="member-success")
]
