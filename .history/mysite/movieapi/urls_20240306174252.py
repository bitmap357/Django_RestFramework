from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('movieapi/', include('movieapi.urls'))
]
