from django.db import models

# Create your models here.
class Courses(models.Model):

    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descriçao', blank=True)
    start_date = models.DateField(
        'Date de inicio', null=True, blank=True
    )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem'
    )
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Criado em', auto_now=True)
