from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<ide>\d+)/$', views.Welcome.as_view(),name="personaje"),
    url(r'^comics/$', views.Comics.as_view()),
    url(r'^$',views.SelectSuper.as_view(), name="home"),
]