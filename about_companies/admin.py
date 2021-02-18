from django.contrib import admin

from .models import Company

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    # In the admin page, slug is in read only
    # readonly_fields = ('slug',) # tuple
    
    # preview the slug
    prepopulated_fields = {'slug': ('name',)} # tuple
    list_filter = ('is_nasdaq', 'year',)
    list_display = ('name', 'year', )

admin.site.register(Company, CompanyAdmin)