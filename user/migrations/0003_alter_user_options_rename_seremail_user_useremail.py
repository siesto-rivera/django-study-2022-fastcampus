# Generated by Django 4.0.3 on 2022-03-03 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_options_user_seremail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='seremail',
            new_name='useremail',
        ),
    ]