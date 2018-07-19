# Generated by Django 2.0.5 on 2018-07-12 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newtest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=20)),
                ('video', models.CharField(max_length=20)),
                ('clientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newtest.Client')),
            ],
        ),
        migrations.DeleteModel(
            name='Version',
        ),
    ]