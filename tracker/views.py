from django.shortcuts import render, redirect
from .models import HealthRecord
from .forms import HealthRecordForm
import calendar
from datetime import datetime
import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def record_health(request):
    # Form
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_health')
    else:
        form = HealthRecordForm()

    # Current month
    today = datetime.today()
    year = today.year
    month = today.month

    # Previous month & Next month
    if 'month' in request.GET:
        selected_month = datetime.strptime(request.GET['month'], '%Y-%m')
        year = selected_month.year
        month = selected_month.month
    
    # get days in month
    _, last_day = calendar.monthrange(year, month)

    # list of day1 ~ last day
    full_dates = [datetime(year, month, day).strftime('%Y-%m-%d') for day in range(1, last_day + 1)]
    dates = [datetime(year, month, day).strftime('%d') for day in range(1, last_day + 1)]

    # Get data for selected month
    records = HealthRecord.objects.filter(date__year=year, date__month=month)

    # Data in dictionary format, storing weight by date.
    weight_data = {record.date.strftime('%Y-%m-%d'): record.weight for record in records}

    # Create a list of data for one month (days with no data are set to None or 0)
    weights = [weight_data.get(date, None) for date in full_dates]


    # get temperature data
    temperature_data = {record.date.strftime('%Y-%m-%d'): float(record.temperature) if record.temperature is not None else None
                        for record in records
                        }

    # make temperature data list
    temperatures = [temperature_data.get(date, None) for date in full_dates]

    # get date if Menstruation
    period_days = [record.date.strftime('%Y-%m-%d') for record in records if record.menstruation]

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'selected_month': f"{year}-{month:02d}",
            'prev_month': f"{year}-{month-1:02d}" if month > 1 else f"{year-1}-12",
            'next_month': f"{year}-{month+1:02d}" if month < 12 else f"{year+1}-01",
            'dates': json.dumps(dates),
            'weights': json.dumps(weights),
            'temperatures': json.dumps(temperatures),
            'period_days': json.dumps(period_days),
        })

    return render(request, 'tracker/record_health.html', {
        'form': form,
        'errors': form.errors.as_json(),
        'records': records,
        'dates': json.dumps(dates),
        'weights': json.dumps(weights),
        'selected_month': f"{year}-{month:02d}",
        'prev_month': f"{year}-{month-1:02d}" if month > 1 else f"{year-1}-12",
        'next_month': f"{year}-{month+1:02d}" if month < 12 else f"{year+1}-01",
        'temperatures': json.dumps(temperatures),
        'period_days': json.dumps(period_days),
    })

    
def delete_record(request, record_id):
    if request.method == 'POST':
        record = get_object_or_404(HealthRecord, id=record_id)
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)


@csrf_exempt
def edit_record(request):
    if request.method == 'POST':
        record = get_object_or_404(HealthRecord, id=request.POST.get('record_id'))
        record.weight = request.POST.get('weight') or None
        record.temperature = request.POST.get('temperature') or None
        record.menstruation = 'menstruation' in request.POST
        record.save()
        return redirect('health_database')


def health_database(request):
    # Current month
    today = datetime.today()
    year = today.year
    month = today.month

    # Previous month & Next month
    if 'month' in request.GET:
        selected_month = datetime.strptime(request.GET['month'], '%Y-%m')
        year, month = selected_month.year, selected_month.month
    
    records = HealthRecord.objects.filter(date__year=year, date__month=month)

    return render(request, 'tracker/health_database.html', {
        'records': records,
        'selected_month': f"{year}-{month:02d}",
        'prev_month': f"{year}-{month-1:02d}" if month > 1 else f"{year-1}-12",
        'next_month': f"{year}-{month+1:02d}" if month < 12 else f"{year+1}-01",
    })