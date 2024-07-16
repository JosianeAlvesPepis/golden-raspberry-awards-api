# Generated by Django 5.0.7 on 2024-07-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('produtor', models.CharField(max_length=255)),
                ('ano', models.IntegerField()),
                ('vencedor', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]