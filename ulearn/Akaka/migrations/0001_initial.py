# Generated by Django 5.0.1 on 2024-01-23 16:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_main1', models.TextField(verbose_name='Текст на главной странице сверху')),
                ('text_main2', models.TextField(verbose_name='Текст на главной странице снизу')),
                ('text_actual1', models.TextField(verbose_name='Текст на странице востребованности зарплат по годам')),
                ('text_actual2', models.TextField(verbose_name='Текст на странице востребованности количества по годам')),
                ('text_actual3', models.TextField(verbose_name='Текст на странице востребованности зарплат по годам для вакансии')),
                ('text_actual4', models.TextField(verbose_name='Текст на странице востребованности количества по годам для вакансии')),
                ('text_geography1', models.TextField(verbose_name='Текст на странице географии зарплат по городам')),
                ('text_geography2', models.TextField(verbose_name='Текст на странице географии количества по городам')),
                ('text_geography3', models.TextField(verbose_name='Текст на странице географии зарплат по городам для вакансии')),
                ('text_geography4', models.TextField(verbose_name='Текст на странице географии количества по городам для вакансии')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название навыка')),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название вакансии')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('area_name', models.TextField(verbose_name='Город')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата создания вакансии')),
            ],
            options={
                'db_table': 'vacancy',
            },
        ),
        migrations.CreateModel(
            name='VacancySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Akaka.skill')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Akaka.vacancy')),
            ],
            options={
                'db_table': 'vacancy_skill',
                'unique_together': {('vacancy', 'skill')},
            },
        ),
    ]
