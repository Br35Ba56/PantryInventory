from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from api.models import Item

class Command(BaseCommand):
        def handle(self, *args, **options):
            user_group, created = Group.objects.get_or_create(name='api_user_group')
            # Code to add permission to group ???
            ct = ContentType.objects.get_for_model(Item)

            permissions = [
                {
                    'codename': 'can_add_item',
                    'name': 'Can add item'
                },
                {
                    'codename': 'can_change_item',
                    'name': 'Can change item'
                },
                {
                    'codename': 'can_delete_item',
                    'name': 'Can delete item'
                },
                {
                    'codename': 'can_view_item',
                    'name': 'Can view item'
                }
            ]

            for permission in permissions:
                user_group.permissions.add(Permission.objects.create(codename=permission['codename'],
                                            name=permission['name'],
                                            content_type=ct))

                        
