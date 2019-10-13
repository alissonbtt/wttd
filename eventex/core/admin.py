from django.contrib import admin
from .models import Speaker

class SpeakerModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Speaker, SpeakerModelAdmin)

# Register your models here.
