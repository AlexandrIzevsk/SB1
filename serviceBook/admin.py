from django.contrib import admin
from .models import Manual, Machine, Service, TO, Reclamation


admin.site.register(Manual)
admin.site.register(Machine)
admin.site.register(Service)
admin.site.register(TO)
admin.site.register(Reclamation)
