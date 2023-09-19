from django.shortcuts import render, get_object_or_404
from .models import Meetings, Rooms

# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, 'meetings/detail.html', {'meeting' : meeting})

def rooms_list(request):
    return render(request, 'meetings/rooms_list.html', {'rooms' : Rooms.objects.all()})
    