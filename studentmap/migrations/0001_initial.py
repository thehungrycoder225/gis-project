# Generated by Django 3.0.5 on 2020-09-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stud_id', models.CharField(max_length=50)),
                ('municipality', models.CharField(max_length=50)),
                ('barangay', models.CharField(max_length=50)),
                ('stud_name', models.CharField(max_length=50)),
                ('stud_age', models.IntegerField(max_length=50)),
                ('stud_pnumber', models.IntegerField(max_length=50)),
                ('stud_course', models.CharField(max_length=50)),
                ('stud_year', models.CharField(max_length=50)),
                ('hlat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('hlong', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
    ]