# Generated by Django 4.1.3 on 2023-05-10 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0004_delete_parkingspace_remove_reservation_parking_spot_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('x_coordinate', models.IntegerField()),
                ('y_coordinate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distances_to', to='parking_app.parkingspace')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distances_from', to='parking_app.parkingspace')),
            ],
        ),
    ]