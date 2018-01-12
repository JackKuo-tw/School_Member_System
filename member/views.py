from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
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
