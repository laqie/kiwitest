from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'KiwiTest.students.views.index', name='index'),
    url(r'^group/(\d+)/$', 'KiwiTest.students.views.group', name='show_group'),
    url(r'^student/add/$', 'KiwiTest.students.views.manage_student', name='add_student'),
    url(r'^student/add/(?P<group_id>\d+)/$', 'KiwiTest.students.views.manage_student', name='add_student_to_group'),
    url(r'^student/edit/(\d+)/$', 'KiwiTest.students.views.manage_student', name='edit_student'),
    url(r'^group/add/$', 'KiwiTest.students.views.manage_group', name='add_group'),
    url(r'^group/edit/(\d+)/$', 'KiwiTest.students.views.manage_group', name='edit_group'),
    
    url(r'^student/delete/(?P<instance_id>\d+)/',
        'KiwiTest.students.views.delete_instance',
        name='delete_student',
        kwargs={'instance_type': 1}),

    url(r'^group/delete/(?P<instance_id>\d+)/',
        'KiwiTest.students.views.delete_instance',
        name='delete_group',
        kwargs={'instance_type': 2}),

    # url(r'^KiwiTest/', include('KiwiTest.foo.urls')),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login/'}),
    (r'^accounts/profile/', 'django.views.generic.simple.redirect_to', {'url': '/'}),
    url(r'^admin/', include(admin.site.urls)),
)
