# Generated by Django 2.2.5 on 2022-09-27 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20220819_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='facility',
            new_name='facilities',
        ),
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
