from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, Accessrecord

# Create your views here.
def index(request):
    webpages_list = Accessrecord.objects.order_by('date')
    myDict = {
        'access_records': webpages_list,
        'name': 'Usamah Abdillah Hanif'
    }
    return render(request, 'first_app/index.html', context=myDict)