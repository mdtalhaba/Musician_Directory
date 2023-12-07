# Generated by Django 4.2.7 on 2023-12-07 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumName', models.CharField(max_length=50)),
                ('albumReleaseDate', models.DateField()),
                ('rating', models.CharField(choices=[('op1', '1'), ('op2', '2'), ('op3', '3'), ('op4', '4'), ('op5', '5')], max_length=5)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician')),
            ],
        ),
    ]