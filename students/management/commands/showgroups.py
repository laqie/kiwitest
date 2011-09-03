from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Show groups and count students in it"

    def handle(self, *args, **options):
        from kiwitest.students.models import Group
        groups = Group.objects.all()

        for group in groups:
            print "%s   \t%d" % (group.title, group.students.count())
        