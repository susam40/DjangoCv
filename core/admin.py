from django.contrib import admin
from core.models import *


@admin.register(GeneralSetting) 
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','description','parameter','updated_date','created_date']
    search_fields=['name','description','parameter']
    list_editable=['description','parameter']
    class Meta:
        model = GeneralSetting
        
@admin.register(ImageSetting) 
class ImageSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','description','file','updated_date','created_date']
    search_fields=['name','description','file']
    list_editable=['description','file']
    class Meta:
        model = ImageSetting
        
@admin.register(Skill) 
class SkillAdmin(admin.ModelAdmin):
    list_display=['id','order','name','percentage','updated_date','created_date']
    search_fields=['name']
    list_editable=['order','name','percentage']
    class Meta:
        model = Skill

@admin.register(Experience) 
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date']
    list_editable = ['job_title', 'job_location']
    search_fields = ['company_name', 'job_title', 'job_location']

    class Meta:
        model = Experience
        
@admin.register(Education) 
class EducationAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'major', 'department', 'start_date', 'end_date']
    list_editable = ['major', 'department']
    search_fields = ['school_name', 'major', 'department']

    class Meta:
        model = Education

