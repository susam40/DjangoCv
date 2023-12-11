from django.db import models

class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True, 
        verbose_name='Name Test',
        help_text='Ayar İsmi'
    )
    
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    updated_date=models.DateTimeField(
        blank=True,
        auto_now=True,
    )
    created_date=models.DateField(
        blank=True,
        auto_now_add=True,
    )
    def __str__(self):
        return 'General Setting:'+self.name
    
    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name', )
        
class ImageSetting(models.Model):
        name = models.CharField(
        default='',
        max_length=254,
        blank=True, 
        verbose_name='Name Test',
        help_text='Ayar İsmi'
    )
        description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        file = models.ImageField(
            default='',
            verbose_name='Image',
            help_text='',
            blank=True,
            upload_to='images/',
        )
        
        updated_date=models.DateTimeField(
        blank=True,
        auto_now=True,
        )
        
        created_date=models.DateTimeField(
        blank=True,
        auto_now_add=True,
        
        )
        
        def __str__(self):
            return 'Image Setting:'+self.name
    
        class Meta:
            verbose_name = 'Image Setting'
            verbose_name_plural = 'Image Setting'
            ordering = ('name', )