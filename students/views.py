# -*-coding: utf-8-*-
from students.models import Group
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
    groups = Group.objects.all()

    data = dict(groups=groups)
    return render_to_response('students/index.html', data)


def group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = group.students.all()

    data = dict(group=group, students=students)
    return render_to_response('students/group.html', data)