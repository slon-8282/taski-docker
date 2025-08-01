from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

from rest_framework import routers  # type: ignore

from api import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
