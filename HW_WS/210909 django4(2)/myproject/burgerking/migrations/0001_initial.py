# Generated by Django 3.2.6 on 2021-09-09 05:40

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Burgerking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=100)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]