from django.shortcuts import render, redirect
from .models import CalorieEntry

def calorie_list(request):
    entries = CalorieEntry.objects.all()
    return render(request, 'myapp/calorie_list.html', {'entries': entries})

def add_calorie(request):
    if request.method == 'POST':
        date = request.POST['date']
        meal = request.POST['meal']
        calorie_count = request.POST['calorie_count']
        entry = CalorieEntry(date=date, meal=meal, calorie_count=calorie_count)
        entry.save()
        return redirect('calorie_list')
    return render(request, 'myapp/add_calorie.html')
