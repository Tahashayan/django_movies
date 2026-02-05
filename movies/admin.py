from django.contrib import admin
from .models import Genre, Movie

class Genreadmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class Movieadmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate')

admin.site.register(Genre, Genreadmin)
admin.site.register(Movie, Movieadmin)
