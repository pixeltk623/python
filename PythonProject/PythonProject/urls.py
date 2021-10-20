"""PythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from crud import views
from mongo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name="index"),
    # path('create/', views.create, name='create'),
    # path('edit/<int:user_id>/', views.edit,name='edit'),
    # path('show/<int:user_id>/', views.show,name='show'),
    # path('update/<int:user_id>/', views.update,name='update'),
    # path('delete/<int:user_id>/', views.delete, name='delete'),

    path('mongo/', views.index, name='delete'),

]
