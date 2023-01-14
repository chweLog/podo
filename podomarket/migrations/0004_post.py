# Generated by Django 2.2 on 2022-10-06 03:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0003_auto_20221005_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('item_price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('item_condition', models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('하', '하')], max_length=10)),
                ('item_details', models.TextField(blank=True)),
                ('image1', models.ImageField(upload_to='item_pics')),
                ('image2', models.ImageField(blank=True, upload_to='item_pics')),
                ('image3', models.ImageField(blank=True, upload_to='item_pics')),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]