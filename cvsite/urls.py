from django.urls import path
from cvsite import views

app_name = "cvsite"

urlpatterns = [
path('',views.index_view,name='index')
]