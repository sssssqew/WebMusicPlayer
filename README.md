# WebMusicPlayer

웹 뮤직 플레이어는 다른 음원도 되지만 멜론에 최적화되어 있습니다. 

```
1.  meta["lyrics"] = meta["lyrics"].replace('"','\\"') # 큰따옴표를 백슬래쉬로 이스케이프
2.  /tmp/mod_wsgi-localhost:8000/httpd.conf 에서 /LimitRequestBody로 검색후 업로드 사이즈 변경 (현재 100MB = 10곡 업로드 가능)
3.  django settings.py 에서 MAX_UPLOAD_SIZE = "5242880" 설정 추가 
```
