#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (
		HttpResponse, 
		HttpResponseRedirect, 
		HttpResponseNotFound,
		Http404
	)

from .models import AudioFile

from django.utils import timezone 
from django.db.models import Sum 

# 음악정보 추출 라이브러리 
from mutagen.id3 import ID3, USLT, TRCK, TIT2, TPE1, TALB, TDRC, TCON, TENC, COMM, APIC, error
from mutagen.mp3 import MP3 

import os 
import time 

# Create your views here.


# 페이지 렌더링은 파일전송 성공시 Ajax 콜백함수(success)에서 한번만 함
# Ajax 콜백함수(success)가 호출되면 페이지를 새로고침함 
# 새로고침하면 아래 함수로 들어와 모든 리소스를 업데이트하고 렌더링함 
def index(request):

	print ("rendering start...")

	try:
		musics = AudioFile.objects.all()
	except:
		musics = None

	context = {"musics":musics}

	return render(request, 'mp3/layout.html', context)
	


# Ajax 콜이 오면 db 에 파일을 저장만 함 
def saveSong(request):

	print ("save files...")


	if request.method == 'POST' and request.FILES:
		print ("request !!")
		
		songs = request.FILES.getlist('songFile')

		for song in songs:
			# print (song.name)

			try:
				audioFile = AudioFile.objects.get(name=song.name)
				print ("\n" + song.name + '  is already exists in database !!')
	 
			except:
				# DB에 음악파일 저장 
				audioFile = AudioFile(song=song, name=song.name)
				audioFile.save()
				print ("\n" + song.name + '  just saved in database !!')

				# 한글깨짐 해결 (mutagen)
				# 터미널에서 updating 이라는 메세지가 나오면서 시간이 오래 걸림 (3초)
				# 저장할때 해당파일만 변경해서 실제 로딩할때는 updating 메시지가 안나옴 
				# 경로에서 mp3/ 제거하니까 됨 
				cmd = 'find ./static/upload -iname "' + audioFile.filename() +'" -execdir mid3iconv -e cp949 {} \;'
				os.system(cmd)

				print ('\n')

	# 파일저장만 하면 되기 때문에 return 값이 없음 
	return HttpResponse("")











