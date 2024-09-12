from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('Capteur', views.CapteurViewSet)
router.register('Incendie', views.IncendieViewSet)
router.register('Zone', views.ZoneViewSet)
urlpatterns = [ path ('', include (router.urls))]