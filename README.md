# WebMusicPlayer

```
웹 뮤직 플레이어는 로컬 PC에 있는 음원 파일을 웹서버에 업로드하여 온라인 상에서 청취할 수 있는 서비스입니다. 
다른 음원도 되지만 멜론에 최적화되어 있습니다. 
현재 아래 깃저장소로 리뉴얼했으니 아래 링크를 클릭해서 설치를 진행해주세요.
https://github.com/sssssqew/webmusicplayer-new
```

```
[issue solution]
1.  meta["lyrics"] = meta["lyrics"].replace('"','\\"') # 큰따옴표를 백슬래쉬로 이스케이프
2.  /tmp/mod_wsgi-localhost:8000/httpd.conf 에서 /LimitRequestBody로 검색후 업로드 사이즈 변경 (현재 100MB = 10곡 업로드 가능)
3.  django settings.py 에서 MAX_UPLOAD_SIZE = "5242880" 설정 추가 
```
