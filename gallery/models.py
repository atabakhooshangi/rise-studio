from django.db import models

CATEGORY_CHOICES = (
    ('wedding', 'wedding'),
    ('birthday', 'birthday'),
    ('engagement', 'engagement')
)


class Members(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    phone_number = models.IntegerField(null=True)
    description = models.TextField(null=True, blank=True)
    instagram = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Members'
        verbose_name_plural = 'Members'


class Photos(models.Model):
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=11, null=True, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='photos', null=True)

    class Meta:
        verbose_name = 'Photos'
        verbose_name_plural = 'Photos'


class Videos(models.Model):
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=11, null=True, choices=CATEGORY_CHOICES)
    video = models.FileField(upload_to='videos', null=True)

    class Meta:
        verbose_name = 'Videos'
        verbose_name_plural = 'Videos'
