# Generated by Django 4.2.6 on 2023-10-12 08:28

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=225)),
                ('venue', models.CharField(max_length=225)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
                ('short_description', tinymce.models.HTMLField()),
                ('long_description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('contact', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=225)),
                ('old_member', models.BooleanField()),
                ('member_id', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_name', models.CharField(max_length=225)),
                ('first_time_charge', models.IntegerField()),
                ('recurring_charge', models.IntegerField()),
                ('renewal_period', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='is_verified',
            new_name='is_email_verified',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_otp_verified',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_registration', models.BooleanField()),
                ('available_from', models.DateTimeField()),
                ('available_to', models.DateTimeField()),
                ('Events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.events')),
            ],
        ),
    ]
