from datetime import date, timedelta
from django.http import HttpResponse
from django.shortcuts import render
#from django.conf import settings
from fremmode.models import Medlemmer, Fremmode
from .db_utils import get_deltager_matrix

# Create your views here.

def next_weekday(fdate, weekday):
    "find next weekday starting fdate"
    days = (weekday-fdate.weekday()) % 7
    day = fdate + timedelta(days=days)
    return day

def get_next_dates(startdate, weekday, number=10):
    "Return list of dates weekday man=0"
    start = next_weekday(startdate, weekday)
    date_list = []
    for i in range(number):
        date_list.append(start + timedelta(days=i*7))
    return date_list

def dates_to_text(datelist):
    "create string of date texts"
    outdate = []
    for this_date in datelist:
        outdate.append(this_date.strftime("%a %d/%m"))
    return outdate

def home(request):
    "home"
    return render(request, 'home.html')

def medlem(request):
    "medlemsoversigt"
    admin = 0
    if admin:
        medlemmer = list(Medlemmer.objects.all().values() )
    else:
        medlemmer = list(Medlemmer.objects.filter(Status=1).order_by('Fornavn').values() )
    return render(request, 'medlems_oversigt.html', context={'admin': admin, 'medlemmer': medlemmer})

def oversigt(request):
    "oversigt"
    weekdays=['Mandag','Tirsdag','Onsdag','Torsdag','Fredag','Lørdag','Søndag']
    dag = request.GET.get('dag',5)
    weekday = int(dag)
    print(str)
    #weekday = 5 # lordag
    start_date = date.today()
    dates = get_next_dates(start_date, weekday, 6)
    datestring = dates_to_text(dates)
    date_list = ['Dato']
    for this_d in datestring:
        date_list.append(this_d)
    medlemmer = Medlemmer.objects.filter(Status=1)
    if True:
        deltagere = medlemmer.filter(Lordag=1).order_by('Fornavn')
    medlems_list = list(deltagere.values_list('Medlemsnummer', flat=True))
    matrix = get_deltager_matrix(medlems_list, dates)
    deltager_list = []
    i = 0
    for d in deltagere:
        name = d.Fornavn + ' ' + d.Efternavn
        entry = [name] + list(matrix[i])
        deltager_list.append(entry)
        i +=1
    total_list = ['Ialt']
    for d in range(len(dates)):
        t = 0
        for s in range(len(deltagere)):
            if matrix[s][d] == 1:
                t +=1
        total_list.append(t)

    context = {'weekday': weekday, 'day': weekdays[weekday], 'dates': dates, 'deltagere': deltager_list, 'matrix': matrix, 'total': total_list}
    return render(request, 'oversigt.html', context=context)

# pylint: disable=unused-argument

def service_worker(request):
    "service worker"
    #sw_path = settings.BASE_DIR / "fremmode/static/js" / "serviceworker.js"
    #response = HttpResponse(open(sw_path, encoding='utf-8').read(), content_type='application/javascript')
    response = HttpResponse("OK")
    return response

def manifest(request):
    "service worker"
    #sw_path = settings.BASE_DIR / "static" / "manifest.json"
    #response = HttpResponse(open(sw_path, encoding='utf-8').read())
    response = HttpResponse("OK")
    return response
