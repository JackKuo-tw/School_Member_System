from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from photologue.models import Gallery
from django.template import RequestContext
import datetime
# Create your views here.
def hello_world(request):
	return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def index(request):
    return HttpResponse('<h1>Django works!</h1>')

def echo_meta(request):
    values = request.META.items()  # 將字典的鍵值對抽出成為一個清單
    #values.sort()                  # 對清單進行排序
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def index(request):
    return render(request, 'relic/index.html')

def photos(request):
    year = datetime.date.today().year - 1  # This year
    show_year = [year, year-1, year-2]  # only show three years's gallery from today
    text = ""
    yGallery = [] # store gallery of three years
    for i in show_year:
        yGallery.append( Gallery.objects.filter(date_added__year=i) )
    count = 0
    gallery_arr = []
    
    for year in range(len(yGallery)):
        for gallery in yGallery[year]:
            photos = gallery.photos.all()
            gallery_date = gallery.date_added
            gallery_date = str(gallery_date.year) + '.' + str(gallery_date.month) + '.' + str(gallery_date.day)
            
            url_arr = []
            for img in photos:
                name = img.image.name
                photo_dic = {'thunb_url' : '', 'url' : img.image.url}
                photo_position = name.find('photos/') + 7
                dot_position = name.rfind('.')
                url = '../media/' + name[:photo_position] + 'cache/' + name[photo_position:dot_position] + '_thumbnail' + name[dot_position:]
                text = text + "<img src='" + url +"' class='thumbnail' >"
                photo_dic['thumb_url'] = url
                url_arr.append(photo_dic)
                count += 1
                if count == 5:
                    break
            gallery_arr_tmp = {'url_arr' : url_arr, 'date' : gallery_date, 'title' : gallery.title, 'id' : gallery.id}
            gallery_arr.append(gallery_arr_tmp)
            count = 0
    #return HttpResponse(text)
    text = '2020'
    return render(request, 'relic/photos.html',locals())

def gallery(request):
    return HttpResponse('hello')