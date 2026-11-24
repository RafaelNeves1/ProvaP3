from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from citricultura.views import LoteViewSet

router = DefaultRouter()
router.register("lotes", LoteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", include("citricultura.urls")),
]

from django.urls import path
from . import views

urlpatterns = [
    path("lotes/", views.lote_list, name="lote_list"),
    path("lotes/novo/", views.lote_create, name="lote_create"),
    path("lotes/<int:id>/", views.lote_detail, name="lote_detail"),
]
