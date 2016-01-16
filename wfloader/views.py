from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse


# Create your views here.

def help_info(request):
    #return redirect('index.html')
    return render(request, 'docs/index.html')

# def get_all_wikifolios_page(request):
#     wikis = get_wikifolios()
#
#
#     return render(request, 'index.html')