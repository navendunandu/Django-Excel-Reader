from django.urls import path
from myapp import views



urlpatterns = [
    path('',views.upload_excel,name="upload_excel"),
]
