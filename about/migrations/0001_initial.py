# Generated by Django 4.2.13 on 2024-08-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('about_image', models.ImageField(upload_to='about_images/')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('about_text', models.TextField()),
            ],
        ),
    ]
