#-*- coding: utf-8 -*-
from django.http import (
		HttpResponse, 
		HttpResponseRedirect, 
		HttpResponseNotFound,
		Http404
	)
 
from django.db import models
import os
import time 

# 음악정보 추출 라이브러리 
from mutagen.id3 import ID3, USLT, TRCK, TIT2, TPE1, TALB, TDRC, TCON, TENC, COMM, APIC, error
from mutagen import File

from django.utils.html import escape
from django.utils.safestring import mark_safe


# Create your models here.
class AudioFile(models.Model):
	# static 앞에 mp3/ 제거하니까 됨 
	song = models.FileField(upload_to='static/upload', null=True) 
	name = models.CharField(max_length=50, null=True)	
	# cover = models.FileField(upload_to='mp3/static/upload/%Y/%m/%d')

	def __str__(self):
		return self.name # class 를 화면에 표시할때 노래제목 사용

	def filename(self):
		return os.path.basename(self.song.file.name)

	def metadata(self):
		
		musicName = os.path.splitext(self.filename())[0] # 확장자를 제외한 파일명 
		# 앨범커버 주소 (static 앞에 / 제거하니까 됨)
		coverURL = 'static/albumCover/'+ musicName + '.jpg'  
		coverDefault = 'static/albumCover/cdp.png'
		titleDefault = os.path.splitext(self.name)[0]

		meta = {"cover": coverDefault, "album": "", "title": titleDefault, "artist": "", "genre": "", "release": "", "encodedby": "", "lyrics": "", "duration": 0}

		if self.song:
			# print (self.song)

			# 메타데이터 추출 
			try:
				mp3 = File(self.song)

				for key in mp3.tags:
					if key == "APIC:Cover" or key == "APIC:":
						# 특정위치의 파일에 태그에서 읽은 앨범커버 이미지를 복사함 
						if not os.path.exists(coverURL):
							with open(coverURL, 'wb') as img:
								img.write(mp3.tags[key].data)
	
						# else:
						# 	print ("cover already exists !!")

						meta["cover"] = coverURL

					if key == "TALB":
						meta["album"] = str(mp3.tags[key])					

					if key == "TIT2":
						meta["title"] = str(mp3.tags[key])
						
					if key == "TPE1":
						meta["artist"] = str(mp3.tags[key])	

					if key == "TCON":
						meta["genre"] = str(mp3.tags[key])
					
					if key == "TDRC":
						meta["release"] = str(mp3.tags[key])
					
					if key == "TENC" or key == "COMM":
						meta["encodedby"] = str(mp3.tags[key])  

				# 더블쿼트 싱글쿼트 문제 해결 (mark_safe 함수 사용)(&#39; -> '')
				# 마치 innerText 일때 &#39; 가 innerHTML 일때 ''로 바뀌는 것과 같음
				try:	
					contents = mark_safe(mp3.tags.getall("USLT"))
					startIdx = contents.find("text=") + 5
					meta["lyrics"] = mark_safe(contents[startIdx+1:len(contents)-3])
					meta["lyrics"] = meta["lyrics"].replace("'", '"')
					
				except:
					print ("lyrics don't exist")			

				meta["duration"] = mp3.info.length

			except:
				print ("There is no mp3 metadata !!")

		else:
			print ("There is no song ");

		# print ("cover : " + meta["cover"])
		# print ("album : " + meta["album"])
		# print ("title : " + meta["title"])
		# print ("artist : " + meta["artist"])
		# print ("genre : " + meta["genre"])
		# print ("release : " + meta["release"])
		# print ("encodedby : " + meta["encodedby"])
		# print ("lyrics : " + meta["lyrics"])
		# print ("duration : " + str(meta["duration"]))

		return meta 
