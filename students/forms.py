#!-*-coding: utf-8-*-
from django.forms import ModelForm, DateField, BooleanField, Form, RadioSelect
from KiwiTest.students.models import Student, Group

class StudentForm(ModelForm):
    birthday = DateField(help_text=u'Например: 1687-03-24', label=u'Дата рождения')
    class Meta:
        model = Student

class GroupForm(ModelForm):
    class Meta:
        model = Group

YES_OR_NO = (
    (True, u'Да, удалить'),
    (False, u'Нет, не удалять')
)
class YesNoForm(Form):
    choice = BooleanField(
        widget=RadioSelect(choices=YES_OR_NO),
        initial=False,
        required=False,
        label=u'Действительно хотите удалить?')