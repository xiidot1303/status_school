from django.shortcuts import render
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def application_registr(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        
        # if form.is_valid():
        form.save()
    form = ApplicationForm()
    context = {'form': form}
    return render(request, 'application/application_registr.html', context)

@login_required
def application_list(request):
    list = Application.objects.all().order_by('-pk')
    context = {'list': list}
    return render(request, 'application/application_list.html', context)