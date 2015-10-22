# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='title',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='description',
            new_name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
    ]
