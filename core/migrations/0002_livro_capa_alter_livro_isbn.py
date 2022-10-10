# Generated by Django 4.1 on 2022-10-10 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0001_initial"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="media.image",
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="isbn",
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]