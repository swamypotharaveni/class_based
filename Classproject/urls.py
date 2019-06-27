from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/',include('myapp.urls')),
    path('registration/',include('django.contrib.auth.urls'))



]
