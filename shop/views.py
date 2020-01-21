import requests
import re
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from .models import Item


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
    canvas = Image.open(io).convert('RGBA')  # 이미지 파일을 열고, RGBA 모드로 변환
    font = ImageFont.truetype(ttf_path, 40)  # 지정 경로의 TrueType 폰트, 폰트크기 40
    draw = ImageDraw.Draw(canvas)  # canvas에 대한 ImageDraw 객체 획득
    text = 'Ask Company'
    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin
    draw.rectangle((left, top, right, bottom), (255, 255, 224))
    draw.text((15, 15), text, font=font, fill=(20, 20, 20))
    response = HttpResponse(content_type='image/png')
    canvas.save(response, format='PNG')  # HttpResponse 의 file-like 특성 활용 return response
    return response


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', "")
    if q:
        qs = qs.filter(name__icontains=q)

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q
    })

def item_detail(request,pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html',{
        'item' : item
    })


def item_new(request, item=None):
    error_list = []
    initial = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        name = data.get('name')
        desc = data.get('desc')
        price = data.get('price')
        photo = files.get('photo')
        is_publish = data.get('is_publish') in (True, 't', 'True', '1')

        # 유효성 검사
        if len(name) < 2:
            error_list.append('name을 2글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', desc):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            # 저장 시도
            if item is None:
                item = Item()

            item.name = name
            item.desc = desc
            item.price = price
            item.is_publish = is_publish

            if photo:
                item.photo.save(photo.name, photo, save=False)

            try:
                item.save()
            except Exception as e:
                error_list.append(e)
            else:
                return redirect(item)  #item.get_absolute_url이 호출됨

        initial = {
            'name': name,
            'desc': desc,
            'price': price,
            'photo': photo,
            'is_publish': is_publish,
        }
    else:
        if item is not None:
            initial = {
                'name': item.name,
                'desc': item.desc,
                'price': item.price,
                'photo': item.photo,
                'is_publish': item.is_publish,
            }

    return render(request, 'shop/item_new.html', {
        'error_list': error_list,
        'initial': initial,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)