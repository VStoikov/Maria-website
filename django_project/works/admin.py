from django.contrib import admin
from .models import Work, ChallanNumber, HSCNumber, Report, QuantityRate, ServiceReport, ServiceChallanNumber

admin.site.register(Work)
admin.site.register(ChallanNumber)
admin.site.register(ServiceChallanNumber)
admin.site.register(HSCNumber)
admin.site.register(Report)
admin.site.register(ServiceReport)
admin.site.register(QuantityRate)