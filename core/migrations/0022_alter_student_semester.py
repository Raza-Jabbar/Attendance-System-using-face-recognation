# Generated by Django 4.2.7 on 2024-04-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_student_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.ManyToManyField(blank=True, related_name='semesters', to='core.semester'),
        ),
    ]
