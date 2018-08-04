from django.contrib import admin

# Register your models here.

from .models import Street
from .models import House
from .models import Appliance
from .models import OperationTimes
from .models import Table_Link

admin.site.register(Street)
admin.site.register(House)
admin.site.register(Appliance)
admin.site.register(OperationTimes)
admin.site.register(Table_Link)
