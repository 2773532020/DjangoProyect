# Generated by Django 5.0.6 on 2024-06-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_posts", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="comments/"),
        ),
    ]
