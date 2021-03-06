# Generated by Django 3.1 on 2020-09-21 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('oil', models.CharField(choices=[('5.000', 'miles'), ('10.000', 'miles'), ('15.000', 'miles'), ('20.000', 'miles'), ('25.000', 'miles'), ('30.000', 'miles'), ('35.000', 'miles'), ('40.000', 'miles'), ('45.000', 'miles'), ('50.000', 'miles'), ('55.000', 'miles'), ('60.000', 'miles')], default='5.000', max_length=15)),
                ('tire_rotation', models.CharField(max_length=15)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
        ),
    ]
