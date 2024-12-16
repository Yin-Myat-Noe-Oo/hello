from django.shortcuts import render
from .models import Destination 
from django.templatetags.static import static
# Create your views here.
def home(request):
    dest1=Destination()
    dest1.name='USA'
    dest1.desc='The City That never Sleeps'
    dest1.uni='NYU'
    dest1.offer=False
    dest1.img=static('images/myhusband.jpg')
    
    dest2=Destination()
    dest2.name='USA'
    dest2.desc='The City That never Sleeps'
    dest2.uni='NYU'
    dest2.offer=False
    dest2.img=static('images/myhusband2.jpg')

    dest3=Destination()
    dest3.name='USA'
    dest3.desc='The City That never Sleeps'
    dest3.uni='NYU'
    dest3.offer=True
    dest3.img=static('images/myhusband.jpg')
    
    dests=[dest1,dest2,dest3]
    return render(request,'home.html',{'dest': dests})