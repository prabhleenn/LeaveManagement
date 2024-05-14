# Generated by Django 4.2 on 2023-09-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_alter_leave_leavetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leavetype',
            field=models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'CL(Half Day)'), ('casual', 'CL(Full Day)'), ('emergency', 'Emergency Leave')], default='sick', max_length=25, null=True),
        ),
    ]
