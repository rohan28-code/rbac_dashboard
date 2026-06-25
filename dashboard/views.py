from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render, redirect

from .models import ProjectData
from .forms import ProjectDataForm

def admin_check(user):
    return user.groups.filter(name='admin').exists()

def normaluser_check(user):
    return user.groups.filter(name='NormalUser').exists()

@login_required
def dashboard(request):
    if admin_check(request.user):
        return render(request, 'dashboard/dashboard.html')
    elif normaluser_check(request.user):
        return redirect('user_dashboard')
    return redirect('login')

@login_required
@user_passes_test(normaluser_check)
def user_dashboard(request):
    projects = ProjectData.objects.all()
    return render(request, 'dashboard/user_dashboard.html', {'projects': projects})

@login_required
@user_passes_test(admin_check)
def project_list(request):
    projects = ProjectData.objects.all()
    return render(request, 'dashboard/project_list.html', {'projects': projects})

@login_required
@user_passes_test(admin_check)
def project_add(request):
    if request.method == 'POST':
        form = ProjectDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectDataForm()
    return render(request, 'dashboard/project_form.html', {'form': form})

@login_required
@user_passes_test(admin_check)
def project_edit(request, id):

    project = ProjectData.objects.get(id=id)

    if request.method == 'POST':

        form = ProjectDataForm(
            request.POST,
            instance=project
        )

        if form.is_valid():
            form.save()
            return redirect('project_list')

    else:

        form = ProjectDataForm(
            instance=project
        )

    return render(
        request,
        'dashboard/project_form.html',
        {'form': form}
    )

@login_required
@user_passes_test(admin_check)
def project_delete(request, id):

    project = ProjectData.objects.get(id=id)

    project.delete()

    return redirect('project_list')


