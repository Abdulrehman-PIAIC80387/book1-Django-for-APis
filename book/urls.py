from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',get_book.as_view(),name='home'),
    path('api/',libraryapi.as_view()),
    path('details/<int:pk>/',details.as_view()),
    path('postlist/',postlist.as_view()),
    path('details_new/<int:pk>/',postdetails.as_view())
    


    
]
