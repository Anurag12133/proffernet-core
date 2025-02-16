# Generated by Django 5.1.4 on 2025-02-10 21:07

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0007_alter_contribution_contribution_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectContribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributed_at', models.DateTimeField(auto_now_add=True)),
                ('contribution_type', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_contributions', to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_contributions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-contributed_at'],
                'unique_together': {('user', 'project')},
            },
        ),
    ]
