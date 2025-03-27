# concerts/views.py
from django.shortcuts import render, get_object_or_404
from .models import Concert

def concert_list(request):
    concerts = Concert.objects.all()
    return render(request, 'concerts/concert_list.html', {'concerts': concerts})

def concert_detail(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)
    return render(request, 'concerts/concert_detail.html', {'concert': concert})
