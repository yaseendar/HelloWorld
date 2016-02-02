__author__ = 'yaseen'

from django.conf.urls import url
from views import AddNameView
from views import DisplayName

urlpatterns = [
    url(r'^$', AddNameView.as_view(), name='name-add'),
    url(r'display/$', DisplayName.as_view(), name='display-name'),
]
