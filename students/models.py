from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=50)
    birthday = models.DateField()
    student_ID = models.CharField(max_length=10)
    student_group = models.ForeignKey('students.Group', blank=True, null=True, related_name='students')

    def __unicode__(self):
        return "%s - %s %s. %s." % (self.student_group.title, self.surname, self.name[0], self.patronymic[0])

    def get_name(self):
        return "%s %s.%s." % (self.surname, self.name[0], self.patronymic[0])

class Group(models.Model):
    title = models.CharField(max_length=200)
    head = models.ForeignKey('students.Student', blank=True, null=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('show_group', (self.pk, ))