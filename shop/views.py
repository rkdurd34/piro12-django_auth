import requests
from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def archives_year(request, year):
    return HttpResponse("{}년도에 대한 내용".format(year))



def response_pillow_image(request):
    ttf_path = '/Library/Fonts/AppleGothic.ttf'
    # 이미지 파일 다운로드 혹은 로컬 디스크 상의 이미지 직접 열기' # 윈도우, 맥: '/Library/Fonts/AppleGothic.ttf'
    # 이미지 파일 다운로드 혹은 로컬 디스크 상의 이미지 직접 열기
    image_url = 'http://www.flowermeaning.com/flower-pics/Calla-Lily-Meaning.jpg'
    res = requests.get(image_url)
    io = BytesIO(res.content)
    io.seek(0)
    # 서버로 HTTP GET 요청하여, 응답 획득
    # 응답의 Raw Body 메모리 파일 객체 BytesIO 인스턴스 생성 # 파일의 처음으로 커서를 이동
    canvas = Image.open(io).convert('RGBA') # 이미지 파일을 열고, RGBA 모드로 변환
    font = ImageFont.truetype(ttf_path, 40) # 지정 경로의 TrueType 폰트, 폰트크기 40 
    draw = ImageDraw.Draw(canvas) # canvas에 대한 ImageDraw 객체 획득
    text = 'Ask Company'
    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin
    draw.rectangle((left, top, right, bottom), (255, 255, 224)) 
    draw.text((15,15), text, font=font, fill=(20, 20, 20))
    response = HttpResponse(content_type='image/png')
    canvas.save(response, format='PNG') # HttpResponse 의 file-like 특성 활용 return response
    return response