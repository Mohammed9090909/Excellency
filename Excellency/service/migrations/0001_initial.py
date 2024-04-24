# Generated by Django 5.0.2 on 2024-04-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('استشارات قانونية', 'Legal Advice'), ('صياغة عقود', 'Drafting Contracts'), ('مذكرات', 'Warrant')], max_length=20)),
            ],
        ),
    ]
