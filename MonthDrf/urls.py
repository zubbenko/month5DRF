from main_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test', views.test_api_view ),
    path('api/v1/firstmodel', views.ads_list_api_view),
    path('api/v1/firstmodel/<int:id>/', views.ads_list_api_view),
]
