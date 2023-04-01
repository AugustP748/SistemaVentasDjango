# Generated by Django 4.1.7 on 2023-03-31 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('productos', '0004_alter_category_updated_alter_product_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.category'),
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]
