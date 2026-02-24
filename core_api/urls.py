from django.urls import path, include
from .routers import router


urlpatterns = [
    path('api-mike/', include(router.urls)),
]