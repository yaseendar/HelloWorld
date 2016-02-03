__author__ = 'yaseen'

from django.conf.urls import url
from views import AddNameView
from views import DisplayName
from views import GenerateDummyToken
from views import AllNames

urlpatterns = [
    url(r'^$', AddNameView.as_view(), name='name-add'),
    url(r'display/$', DisplayName.as_view(), name='display-name'),
    url(r'api/display/allnames/$', AllNames.as_view(), name='display-allnames'),
    url(r'api/dummytoken/$', GenerateDummyToken.as_view(), name='dummy-token'),
]
