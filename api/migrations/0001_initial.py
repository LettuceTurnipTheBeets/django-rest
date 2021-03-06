# Generated by Django 2.0.4 on 2018-04-20 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('commonName', models.CharField(max_length=20)),
                ('scientificName', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=20)),
                ('imageURL', models.URLField()),
            ],
        ),
    ]
