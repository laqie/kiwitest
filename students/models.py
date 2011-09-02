# -*-coding: utf-8-*-
from django.db import models

class Student(models.Model):
    surname = models.CharField(verbose_name=u'Фамилия', max_length=100)
    name = models.CharField(verbose_name=u'Имя', max_length=50)
    patronymic = models.CharField(verbose_name=u'Отчество', max_length=50)
    birthday = models.DateField(verbose_name=u'Дата рождения')
    student_ID = models.CharField(verbose_name=u'№ зачетки', max_length=10)
    student_group = models.ForeignKey('students.Group', verbose_name=u'Группа', blank=True, null=True, related_name='students')

    def __unicode__(self):
        return "%s - %s %s. %s." % (self.student_group.title, self.surname, self.name[0], self.patronymic[0])

    def get_name(self):
        return "%s %s.%s." % (self.surname, self.name[0], self.patronymic[0])

    @models.permalink
    def get_edit_url(self):
        return  'edit_student', (self.pk, )

    @models.permalink
    def get_delete_url(self):
        return 'delete_student', (self.pk, )

    class Meta:
        ordering = ('student_group', 'surname')

class Group(models.Model):
    title = models.CharField(verbose_name=u'Название', max_length=200)
    head = models.ForeignKey('students.Student', verbose_name=u'Староста', blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'show_group', (self.pk, )

    @models.permalink
    def get_edit_url(self):
        return  'edit_group', (self.pk,)

    @models.permalink
    def get_delete_url(self):
        return 'delete_group', (self.pk, )

    class Meta:
        ordering = ('title', )