from django.contrib import admin

# Register your models here.
from .models import Superheroes,Musician,Album
class MusicianAdmin(admin.ModelAdmin):
    ordering = ['last_name']
    list_display=['first_name','last_name' ,'instrument']
    search_fields = ['instrument']         #create search box


class AlbumAdmin(admin.ModelAdmin):
    ordering = ['name']                   #it is used for sorting i.e it will sort by name
    list_display = ['artist','name','release_date', 'num_stars']
    list_filter = (('release_date', 'num_stars'))  #filter wrt release date and num_star

class SuperheroesAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name','real_name','comics','powers']

admin.site.register(Superheroes,SuperheroesAdmin)
admin.site.register(Musician,MusicianAdmin)
admin.site.register(Album,AlbumAdmin)
