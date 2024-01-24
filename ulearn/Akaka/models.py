from django.db import models
import datetime




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

