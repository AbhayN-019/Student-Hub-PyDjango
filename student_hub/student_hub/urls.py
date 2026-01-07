"""
URL configuration for student_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from stdhub_app.views import student_create,student_update,student_list,student_delete,greet,view_single_student


urlpatterns = [
    path('admin/', admin.site.urls),
    path('std_hub/',greet,name='homepage'),
    path('student_post/', student_create, name='student_add'),
    path('student_list/', student_list, name='student_list'),
    path('single_student/<int:id>/', view_single_student, name='student_detail'),
    path('update_student/<int:id>/', student_update, name='student_update'),
    path('delete_student/<int:id>/', student_delete, name='student_delete')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
