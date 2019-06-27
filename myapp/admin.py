from django.contrib import admin
from myapp.models import Employee




class emploAdmin(admin.ModelAdmin):
    list_display = ['id','eid','ename','eemail','econtact','uplode_images']

admin.site.register(Employee,emploAdmin)


