# Generated by Django 4.0.3 on 2022-03-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자'},
        ),
        migrations.AddField(
            model_name='user',
            name='seremail',
            field=models.EmailField(default='abc@test.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
