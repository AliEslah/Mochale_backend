from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Mochale Admin Page"
admin.site.index_title = "Model Management"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
