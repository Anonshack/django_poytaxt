from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import F
from django.http import HttpResponse

from .models import HomePage


class HomePageView(ListView):
    def get(self, request):
        context = {}
        clay = HomePage.objects.all()
        context['temp'] = clay
        return render(request, 'home.html', {'temp': clay})


# class ViloyatView(ListView):
#     def get(self, request, pk):
#         context = {}
#         context['add'] = HomePage.objects.filter(id=pk)
#         return render(request, 'viloyat.html', context)
#

class TumanListView(ListView):
    template_name = 'viloyat.html'

    def get_queryset(self):
        try:
            lang = self.request.session['lang']
        except:
            lang = 'uz'
        queryset = HomePage.objects.all().values('name_' + lang, 'description_' + lang).annotate(
            name=F('name_' + lang), description=F('description_' + lang))
        return queryset


def setLanguage(request, lang):
    try:
        request.session['lang'] = lang
        return HttpResponse('OK')
    except:
        return HttpResponse('Error')

