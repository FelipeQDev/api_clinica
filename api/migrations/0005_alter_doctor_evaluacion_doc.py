# Generated by Django 4.1 on 2022-12-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_doctor_evaluacion_doc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="evaluacion_doc",
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
    ]
