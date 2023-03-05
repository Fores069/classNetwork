from django.db import models
from django.urls import reverse


class Posts(models.Model):
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    date_posted = models.DateField()
    description = models.TextField()
    file = models.FileField(upload_to='files/', blank=True)

    def __str__(self):
        return f"{self.cat}{self.pk}"

    class Meta:
        verbose_name = 'Дом. задание'
        verbose_name_plural = 'Дом. задания'

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',kwargs={'cat_slug': self.slug})