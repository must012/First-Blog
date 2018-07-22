from django.db import models as md
from django.utils import timezone as tz
from django.shortcuts import reverse


# Create your models here.

class Board(md.Model):
    title = md.CharField(max_length=200)
    description = md.CharField('DESCRIPTION', max_length=100, blank=True,
                                   help_text='simple description txt')
    text = md.TextField("CONTENT")
    create_date = md.DateTimeField('Create Date', auto_now_add=True)
    modify_date = md.DateTimeField('Modify Date', auto_now=True)
    # 괄호안에 들어가는 문자열(예로들면 published titme)은 레이블이라고 하며
    # 폼 화면에 나타나는 문구이고, admin 사이트에서 확인 가능

    class Meta:
        db_table = 'homepage'
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = tz.now()
        self.save()

    def get_absolute_url(self):
        return reverse('homepage:detail', args=(self.id,))

    def get_previous_post(self):
        return self.get_previous_in_order()

    def get_next_post(self):
        return self.get_next_in_order()