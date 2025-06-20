from django.http import
from FirstApp import views

urlpatterns=[

    url(r'^$', view.index, name='index'),
]
