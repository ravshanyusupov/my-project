# Generated by Django 3.2.9 on 2022-07-01 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='main',
            name='img',
            field=models.ImageField(blank=True, upload_to='backend_images/main_table'),
        ),
        migrations.CreateModel(
            name='MainId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
                ('main_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.main')),
            ],
        ),
    ]