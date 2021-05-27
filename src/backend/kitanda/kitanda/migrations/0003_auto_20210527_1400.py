# Generated by Django 3.2.3 on 2021-05-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitanda', '0002_auto_20210520_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='market',
            name='bank',
            field=models.CharField(max_length=250, null=True, verbose_name='banco'),
        ),
        migrations.AddField(
            model_name='market',
            name='bank_account',
            field=models.CharField(max_length=250, null=True, verbose_name='conta do banco'),
        ),
        migrations.AddField(
            model_name='market',
            name='bank_agency',
            field=models.CharField(max_length=250, null=True, verbose_name='agência do banco'),
        ),
        migrations.AddField(
            model_name='market',
            name='pix',
            field=models.CharField(max_length=250, null=True, verbose_name='pix'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='imagem do produto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='market',
            name='cnpj',
            field=models.CharField(max_length=14, null=True, verbose_name='cnpj'),
        ),
        migrations.AlterField(
            model_name='market',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='market',
            name='latitude',
            field=models.CharField(max_length=250, null=True, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='market',
            name='localization',
            field=models.CharField(max_length=250, null=True, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='market',
            name='longitude',
            field=models.CharField(max_length=250, null=True, verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='market',
            name='name',
            field=models.CharField(max_length=250, null=True, verbose_name='nome'),
        ),
    ]