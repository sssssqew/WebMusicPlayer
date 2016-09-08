#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views as mp # namespace 를 지정하면 urls.py를 열었을때 어느 모듈인지 구분하기 쉬움 


app_name = 'mp3'
urlpatterns = [
	url(r'^$', mp.index, name='home'),
	url(r'^pass/$', mp.saveSong),
	# url(r'^areas/(?P<area>[가-힣]+)/$', mp.areas),
	# url(r'^areas/(?P<area>[가-힣]+)/results$', mp.results),
	# url(r'^polls/(?P<poll_id>\d+)/$', mp.polls),
	# url(r'^candidates/(?P<name>[가-힣]+)/$', mp.candidates)
]
