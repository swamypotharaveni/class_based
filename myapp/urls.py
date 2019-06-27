
from django.urls import path
from myapp.views import createviews,listlsviews,deleteviw


urlpatterns = [

    path('create/',createviews.as_view(),name='create'),
    path('list/',listlsviews.as_view(),name='list'),
    path('delete/<int:pk>/',deleteviw.as_view()),


]
