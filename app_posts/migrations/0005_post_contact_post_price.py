# Generated by Django 5.0.6 on 2024-06-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_posts", "0004_post_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="contact",
            field=models.TextField(default="default_value", max_length=15),
        ),
        migrations.AddField(
            model_name="post",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]
