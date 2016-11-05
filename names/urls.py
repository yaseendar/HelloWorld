__author__ = 'yaseen'

from django.conf.urls import url
from views import ImageToText

urlpatterns = [
    url(r'^$', ImageToText.as_view(), name='name-add'),

]
