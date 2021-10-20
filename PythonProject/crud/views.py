from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.shortcuts import redirect

# from .models import User




# Create your views here.
def index(request):
    #return render(request, 'index.html')
    thisdict = models.User.objects.all()

    print(thisdict)
    #return HttpResponse('<h1>Page was found</h1>')
    return render(request, 'index.html', {'data': thisdict})

def create(request):
    e = ''
    m= ''
    if request.method=='POST':
        formValue = request.POST
        print(request.FILES)
        handle_uploaded_file(request.FILES['fileUpload'])  
        if formValue['name']=='':
            e = "Not Blank"
        else:
            e = ''
        #print(formValue['name'])
            p = models.User(name=formValue['name'])
            p.save()
            r = True
            
            if r==True:
                m = {'class':'alert-success', 'message': 'Data Inserted'}
            else:
                m = {'class':'alert-danger', 'message': 'Error'}
    return render(request, 'create.html', {'error': e, 'message': m})

def delete(request, user_id):
    # thisdict = models.User.objects.all()
    p = models.User(id=user_id)
    
    if p.delete():
        
        return redirect('/')
    else:
        return HttpResponse('<h1>Page was found</h1>')

def edit(request, user_id):
    e = models.User.objects.get(id=user_id)
    #print(e.name)
    return render(request, 'edit.html', {'data':e})

def update(request, user_id):
    if request.method=='POST':
        formValue = request.POST
        print(formValue)
        p = models.User(name=formValue['name'], id = user_id)
        p.save()
    return redirect('/')

def show(request, user_id):
    e = models.User.objects.get(id=user_id)    
    return render(request, 'show.html', {'data':e})


def handle_uploaded_file(f):  
    with open('crud/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 