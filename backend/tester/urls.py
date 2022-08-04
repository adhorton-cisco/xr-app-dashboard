from django.urls import path, re_path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('packages/', views.all_packages),
    path('packages/<int:id>', views.package_id),
    path('packages/<str:name>', views.package_name)
]