from django.db import models
import hashlib
import datetime



class Vacancy(models.Model):
    name = models.TextField("Название вакансии")
    salary = models.IntegerField("Зарплата")
    area_name = models.TextField("Город")
    created_at = models.DateTimeField("Дата создания вакансии", default=datetime.datetime.now)
    skills_list = []


    @property
    def skills(self):
        return [skill.skill.name for skill in VacancySkill.objects.filter(vacancy=self)]

    class Meta:
        db_table = 'vacancy'


class Skill(models.Model):
    name = models.CharField("Название навыка", max_length=64)

    class Meta:
        db_table = 'skill'


class VacancySkill(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('vacancy', 'skill')
        db_table = 'vacancy_skill'

class Content(models.Model):
    text_main1 = models.TextField(verbose_name='Текст на главной странице сверху')
    text_main2 = models.TextField(verbose_name='Текст на главной странице снизу')
    text_actual1 = models.TextField(verbose_name='Текст на странице востребованности зарплат по годам')
    text_actual2 = models.TextField(verbose_name='Текст на странице востребованности количества по годам')
    text_actual3 = models.TextField(verbose_name='Текст на странице востребованности зарплат по годам для вакансии')
    text_actual4 = models.TextField(verbose_name='Текст на странице востребованности количества по годам для вакансии')
    text_geography1 = models.TextField(verbose_name='Текст на странице географии зарплат по городам')
    text_geography2 = models.TextField(verbose_name='Текст на странице географии количества по городам')
    text_geography3 = models.TextField(verbose_name='Текст на странице географии зарплат по городам для вакансии')
    text_geography4 = models.TextField(verbose_name='Текст на странице географии количества по городам для вакансии')

