# WebMusicPlayer

meta["lyrics"] = meta["lyrics"].replace('"','\\"') # 큰따옴표를 백슬래쉬로 이스케이프
/tmp/mod_wsgi-localhost:8000/httpd.conf 에서 /LimitRequestBody로 검색후 업로드 사이즈 변경 (현재 100MB = 10곡 업로드 가능)
django settings.py 에서 MAX_UPLOAD_SIZE = "5242880" 설정 추가 
