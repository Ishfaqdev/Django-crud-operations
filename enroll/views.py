from django.shortcuts import render, HttpResponseRedirect
from . forms import RegistrationForm
from .  models import User
# Create your views here.


def add_display(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            form = RegistrationForm()
    else:
        form = RegistrationForm()
    row = User.objects.all()
    return render(request, 'enroll/add_show.html', {"form": form, "stu": row})


def delete_data(request, id):
    if request.method == 'POST':
        dele = User.objects.get(pk=id)
        dele.delete()
        return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == 'POST':
        update = User.objects.get(pk=id)
        form = RegistrationForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        update = User.objects.get(pk=id)
        form = RegistrationForm(instance=update)
    return render(request, 'enroll/update.html', {'form': form})
