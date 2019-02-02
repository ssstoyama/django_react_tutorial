from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.LeadList)

urlpatterns = [
    path('api/lead/', include(router.urls)),
]