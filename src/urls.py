"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from location.views import my_ip_address, my_location
from review.api.viewsets import ReviewViewSet
from tourist_place.api.viewsets import TouristPlaceViewSet

router = routers.SimpleRouter()
router.register(r"touristplaces", TouristPlaceViewSet, basename="TouristPlace")
router.register(r"reviews", ReviewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path(
        "api/auth/token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="token_auth_obtain_pair",
    ),
    path(
        "api/auth/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_auth_refresh",
    ),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    path("geo-location/check", my_location, name="geo-location-check"),
    path("geo-location/my-ip-address", my_ip_address, name="my-ip-address"),
]
