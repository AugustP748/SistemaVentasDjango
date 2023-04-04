# Generated by Django 4.1.7 on 2023-04-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direcciones', '0001_initial'),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('state', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.ManyToManyField(to='direcciones.address')),
                ('categories', models.ManyToManyField(to='categorias.category')),
            ],
            options={
                'verbose_name': 'Provider',
                'verbose_name_plural': 'Providers',
            },
        ),
    ]