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
