from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core import views


urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),

    # Home
    path("", views.home, name="home"),

    # Articles
    path("articles/", views.article_list, name="article_list"),
    path("articles/<str:slug>/", views.article_detail, name="article_detail"),

    # Equipment
    path("equipment/", views.equipment_list, name="equipment_list"),
    path("equipment/<str:slug>/", views.equipment_detail, name="equipment_detail"),

    # Trainers
    path("trainers/", views.trainer_list, name="trainer_list"),
    path("trainers/<str:slug>/", views.trainer_detail, name="trainer_detail"),

    # Catalogs
    path("catalogs/", views.catalog_list, name="catalog_list"),
]


# Serve uploaded media files during local development.
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
