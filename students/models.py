# -*-coding: utf-8-*-
from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

class Group(models.Model):

    title = models.CharField(verbose_name=u'Название', max_length=200)
    head = models.ForeignKey('students.Student',
                             verbose_name=u'Староста',
                             blank=True,
                             null=True,
                             on_delete=models.SET_NULL)

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


class Student(models.Model):

    surname = models.CharField(verbose_name=u'Фамилия', max_length=100)
    name = models.CharField(verbose_name=u'Имя', max_length=50)
    patronymic = models.CharField(verbose_name=u'Отчество', max_length=50)
    birthday = models.DateField(verbose_name=u'Дата рождения')
    student_ID = models.CharField(verbose_name=u'№ зачетки', max_length=10)
    student_group = models.ForeignKey('students.Group', verbose_name=u'Группа', blank=True, null=True, related_name='students')

    def __unicode__(self):
        try:
            return "%s - %s %s. %s." % (self.student_group.title, self.surname, self.name[0], self.patronymic[0])
        except Group.DoesNotExist:
            return "%s %s. %s." % (self.surname, self.name[0], self.patronymic[0])


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

        

TYPES = (
    ('C', 'Created'),
    ('M', 'Modified'),
    ('D', 'Deleted')
)

class Log(models.Model):

    create_date = models.DateTimeField('Date', auto_now=True)
    type = models.CharField('Type', choices=TYPES, max_length=1)
    model = models.CharField('Class', max_length=200)
    log = models.CharField('Log', max_length=250)

    def __unicode__(self):
        return "%s: %s" % (self.create_date.strftime("%d.%m.%Y %H:%M"), self.log)


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Group)
def model_save_signal(sender, instance, signal, *args, **kwargs):
    h = Log()
    h.model = str(sender)
    h.log = 'Object <%s> with ID <%d> ' % (instance, instance.pk)

    try:
        sender.objects.get(pk=instance.pk)
        h.type = 'M'
        h.log += 'modified'

    except sender.DoesNotExist:
        h.type = 'C'
        h.log += 'created'
        
    h.save()


@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def model_delete_signal(sender, instance, signal, *args, **kwargs):
    h = Log()
    h.model = str(sender)
    h.type = 'D'
    h.log = 'Object <%s> with ID <%d> was deleted' % (instance, instance.pk)
    h.save()

