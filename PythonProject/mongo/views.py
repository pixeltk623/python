from django.shortcuts import render

# Create your views here.

def index(request):
    #return render(request, 'index.html')
    # thisdict = models.User.objects.all()

    #print(thisdict)
    #return HttpResponse('<h1>Page was found</h1>')
    return render(request, 'index.html')
