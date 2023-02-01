from django.shortcuts import render,redirect
from curd.models import details
# Create your views here.
def base_page(request):
    if request.method=="POST":
        Name=request.POST['Name']
        Email=request.POST['Email']
        Phone=request.POST['Phone']
        Country=request.POST['Country']
        City=request.POST['City']
        Query=request.POST['Query']
        
        obj=details.objects.create(Name=Name,Email=Email,Phone=Phone,Country=Country,City=City,Query=Query)
        
        obj.save()
        return redirect('/')
        
    return render(request,'base.html')

def About_page(request):
    return render(request,'About.html')

def Menu_page(request):
    return render(request,'menu.html')
def Python_ide(request):
    return render(request,'python.html')