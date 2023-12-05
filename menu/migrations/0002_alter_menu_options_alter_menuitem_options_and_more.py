# Generated by Django 4.2.7 on 2023-11-30 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['name'], 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['name'], 'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='url',
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование меню'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_itmes', to='menu.menu', verbose_name='Основное меню'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem', verbose_name='Родительский пункт подменю'),
        ),
    ]
