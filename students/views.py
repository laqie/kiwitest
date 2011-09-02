# -*-coding: utf-8-*-
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from students.models import Group, Student
from students.forms import StudentForm, GroupForm, YesNoForm

def index(request):
    
    groups = Group.objects.all()

    data = dict(groups=groups)
    return render_to_response('students/index.html',
                              data,
                              context_instance=RequestContext(request))


def group(request, group_id):

    group = get_object_or_404(Group, pk=group_id)
    students = group.students.all()

    data = dict(group=group, students=students)
    return render_to_response('students/group.html',
                              data,
                              context_instance=RequestContext(request))


@login_required(login_url='/login/')
def manage_student(request, student_id=None, group_id=None):

    if student_id:
        student = get_object_or_404(Student, pk=student_id)
    else:
        student = None

    if group_id:
        group = get_object_or_404(Group, pk=group_id)
    else:
        group = None


    if request.method == 'POST':
        
        if student:
            form = StudentForm(request.POST, instance=student)
        else:
            form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        if student:
            form = StudentForm(instance=student)
        else:
            form = StudentForm(initial={'student_group': group})
            
    data = dict(form=form, student_id=student_id)
    return render_to_response('students/add_student.html',
                              data,
                              context_instance=RequestContext(request))


@login_required(login_url='/login/')
def manage_group(request, group_id=None):

    if group_id:
        group = get_object_or_404(Group, pk=group_id)
    else:
        group = None

    if request.method == 'POST':
        if group:
            form = GroupForm(request.POST, instance=group)
        else:
            form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        if group:
            form = GroupForm(instance=group)
        else:
            form = GroupForm()

    data = dict(form=form, group_id=group_id)
    return render_to_response('students/add_group.html',
                              data,
                              context_instance=RequestContext(request))


@login_required(login_url='/login/')
def delete_instance(request, instance_id, instance_type):
    if instance_type == 1:
        instance = get_object_or_404(Student, pk=instance_id)
    else:
        instance = get_object_or_404(Group, pk=instance_id)



    if request.method == 'POST':
        form = YesNoForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            if choice == True:
                instance.delete()
        return redirect('index')
    else:
        form = YesNoForm()
    data = dict(form=form, instance_id=instance_id, instance=instance, instance_type=instance_type)
    return render_to_response('students/delete_instance.html',
                              data,
                              context_instance=RequestContext(request))

