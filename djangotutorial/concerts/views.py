# concerts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ConcertForm
from .models import Concert
import plotly.express as px
import pandas as pd

def concert_list(request):
    concerts = Concert.objects.all()
    return render(request, 'concerts/concert_list.html', {'concerts': concerts})

def concert_detail(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)
    return render(request, 'concerts/concert_detail.html', {'concert': concert})

def concert_report(request):
    concerts = Concert.objects.all()
    data = {
        'Artist': [concert.artist for concert in concerts],
        'Date': [concert.date for concert in concerts],
        'Venue': [concert.venue for concert in concerts],
        'Price': [concert.price for concert in concerts],
    }
    df = pd.DataFrame(data)

    fig = px.bar(df, x='Artist', y='Price', color='Venue', title='Concert Prices by Artist')
    graph = fig.to_html(full_html=False)

    return render(request, 'concerts/report.html', {'graph': graph})

def create_concert(request):
    if request.method == 'POST':
        form = ConcertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_list')
    else:
        form = ConcertForm()
    return render(request, 'concerts/create_concert.html', {'form': form})