# Generated by Django 4.2.6 on 2024-01-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_part_partimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='sellerID',
            field=models.ManyToManyField(related_name='seller', to='storage.seller'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='carID',
            field=models.ManyToManyField(related_name='carImages', to='storage.car'),
        ),
        migrations.AlterField(
            model_name='part',
            name='sellerID',
            field=models.ManyToManyField(related_name='partSeller', to='storage.seller'),
        ),
        migrations.AlterField(
            model_name='partimage',
            name='partID',
            field=models.ManyToManyField(related_name='partImages', to='storage.part'),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='userID',
            field=models.ManyToManyField(related_name='userIDsPurchase', to='storage.user'),
        ),
    ]
