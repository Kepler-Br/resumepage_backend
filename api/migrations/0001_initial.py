# Generated by Django 2.2.7 on 2019-11-18 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('githubUrl', models.CharField(max_length=100)),
                ('images', models.ManyToManyField(related_name='api_projectmodel_related_images', to='api.ImageModel')),
                ('titleImage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_projectmodel_related_title', to='api.ImageModel')),
            ],
        ),
    ]