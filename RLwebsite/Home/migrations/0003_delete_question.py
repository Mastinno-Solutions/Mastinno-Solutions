# Generated by Django 4.2.19 on 2025-03-06 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_question_category_alter_question_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
