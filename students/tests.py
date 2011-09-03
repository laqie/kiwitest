"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from kiwitest.students.models import Group, Student

class AddRemoveObjects(TestCase):

    group = dict (
        title = 'TestGroup'
    )
    student = dict(
        name='TestName',
        surname='TestSurname',
        patronymic='TestPatronymic',
        birthday='1987-07-08',
        student_ID='ID-234567',
        student_group='1'
    )
    username = 'TestUser'
    password = 'TestPassword'
    email = 'user@example.com'

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(self.username, self.email, self.password)
        
    def test_user_login(self):

        #login by username
        status =  self.client.login(username=self.username, password=self.password)
        self.assertEqual(status, True)

        #login by email
        status =  self.client.login(username=self.email, password=self.password)
        self.assertEqual(status, True)

    def test_add_student_group(self):
        """
        Add group in site and add student in that group
        """

        #login to site
        self.client.login(username=self.username, password=self.password)

        #add group by POST request
        response = self.client.post('/group/add/', self.group)
        self.assertEqual(response.status_code, 302)

        #get added group from db
        group = Group.objects.get(title=self.group['title'])
        self.student['student_group'] = group.pk

        #add student in added group
        response = self.client.post('/student/add/', self.student)
        self.assertEquals(response.status_code, 302)

        #check student's grou is our added group
        student = Student.objects.get(student_ID=self.student['student_ID'])
        self.assertEqual(student.student_group, group)




