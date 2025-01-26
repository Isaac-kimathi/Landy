from django.shortcuts import render, get_object_or_404
from .models import LandRecord

def home(request):
    records = LandRecord.objects.all()
    return render(request, 'landie/home.html', {'records': records})

def land_detail(reuest, pk):
    record = get_object_or_404(LandRecord, pk=pk)
    return render(request, 'landie/land_detail.html', {'record': record})

def register(request):
    return render(request, 'landie/register.html')

