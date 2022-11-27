from django.urls import path
from fremmode import views

urlpatterns = [
  path("", views.home, name="index"),
  path("medlem", views.medlem, name="medlem"),
  path("oversigt", views.oversigt, name="oversigt"),

  #path("serviceworker.js", views.service_worker),
  #path("manifest.json", views.manifest)
  ]
