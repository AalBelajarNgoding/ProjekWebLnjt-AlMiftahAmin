# Generated by Django 4.2.10 on 2024-06-17 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("berita", "0002_alter_artikel_options_alter_kategori_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="artikel",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
