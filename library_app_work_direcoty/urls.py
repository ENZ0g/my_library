"""library_app_work_direcoty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from LIB_APP import views


urlpatterns = [
    path('', views.books_list, name='main'),
    path('admin/', admin.site.urls),
    path('redactions/', views.redactions_list, name='redactions'),
    path('book_increment/', views.book_increment),
    path('book_decrement/', views.book_decrement),
    path('new_book/', views.new_book),
    path('authors/', views.author_list, name='authors'),
    path('readers/', views.readers_list, name='readers')
]
