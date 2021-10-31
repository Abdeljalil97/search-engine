from django.shortcuts import render, redirect
from SearchEngine.search import run

def homepage(request):
    return render(request,'home.html')


def results(request):
    if request.method == "POST":
        result = request.POST.get('search')
        run(result)

        if result == '':
            return redirect('Home')
        else:
            return render(request,'results.html',{'google': None, 'yahoo': None, 'duck': None, 'ecosia': None,'bing': None, 'givewater': None})