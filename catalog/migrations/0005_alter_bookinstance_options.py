# Generated by Django 4.0.2 on 2022-02-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
