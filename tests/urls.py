try:
    from django.urls import re_path as url
except ImportError:
    from django.conf.urls import url
from django.views.generic import View

urlpatterns = [
    url(r'^test/(?P<number>\d+)/$', View.as_view(), name='test'),
]
