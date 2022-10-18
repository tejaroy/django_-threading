# views.py
from django.shortcuts import render, redirect

from Apps.App.models import Emp
from djangoProject.forms import EmpForm

def home(request):
    return render(request, 'home.html')

def email(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('empdata')
            except:
                pass
    else:
        form = EmpForm()
    return render(request, 'email.html', {"form": form})


def empdata(request):
    object = Emp.objects.all()
    return render(request, 'empdata.html', {'object': object})


def update_data(request, id):
    object = Emp.objects.get(id=id)
    if request.POST:
        if object:
            object.Empcode = request.POST['Empcode']
            object.Name =request.POST['Name']
            object.DOBirth =request.POST['DOBirth']
            object.DOJoining = request.POST['DOJoining']
            object.DOAnniversary = request.POST['DOAnniversary']
            object.Email = request.POST['Email']
            object.save()
        # form = EmpForm(request.POST, instance=object)
        # if form.is_valid():
        #     form.save()
        return redirect('empdata')
    else:
        form = EmpForm(instance=object)
    return render(request, 'editdata.html', {'object': object})


def delete_data(request, id):
    object = Emp.objects.get(id=id)
    object.delete()
    return redirect('empdata')
