# Generated by Django 3.2.16 on 2022-12-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_alter_scinfo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='native_p',
            field=models.CharField(max_length=10, verbose_name='籍贯'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=10, verbose_name='姓名'),
        ),
    ]
