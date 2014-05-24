from django.contrib import admin
from pacman.models import Distribution
from pacman.models import Mirror
from pacman.models import Mirror_Distribution

admin.site.register(Distribution)
admin.site.register(Mirror)
admin.site.register(Mirror_Distribution)
