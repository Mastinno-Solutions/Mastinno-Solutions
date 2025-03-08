# Generated by Django 5.1 on 2024-08-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Science', 'Science'), ('Maths', 'Maths'), ('Financial', 'Financial'), ('Maths', 'Maths')], max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/Questions/'),
        ),
    ]
