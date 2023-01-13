# Generated by Django 4.1.1 on 2023-01-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_booklist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booklist",
            name="date_finished",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="booklist",
            name="rating",
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
