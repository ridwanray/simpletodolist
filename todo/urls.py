 
from django.urls import path
from . import views
#from users import views as user_views

app_name= 'todo'
urlpatterns = [
	path('', views.allview, name='alltodoview'),#
    path('addnewtodo', views.addtodo, name='newtodo'),#
]