from django.contrib import admin
from .models import Act, Concert, ConcertInstance

# Register your models here.
admin.site.register(Concert)
admin.site.register(Act)
admin.site.register(ConcertInstance)
