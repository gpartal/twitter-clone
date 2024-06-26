# Generated by Django 5.0.1 on 2024-03-12 09:41

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150, verbose_name='İsim Soyisim')),
                ('bio', models.TextField(default='Merhaba Ben Twitter kullanıyorum', max_length=300, verbose_name='Hakkımda')),
                ('image', models.ImageField(upload_to='profiles/', verbose_name='Profil Resmi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Katılma Tarihi')),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
                ('follow', models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takip Edilenler')),
                ('follower', models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takipçiler')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profiller',
                'ordering': ['-created_at'],
            },
        ),
    ]
