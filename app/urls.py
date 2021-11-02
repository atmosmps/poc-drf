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
from django.urls import path, include
from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token

from address.api.viewsets import AddressViewSet
from core.api.viewsets import TouristPlaceViewSet
from rating.api.viewsets import RatingViewSet
from resource.api.viewsets import ResourceViewSet
from review.api.viewsets import ReviewViewSet
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'touristplaces', TouristPlaceViewSet, basename='TouristPlace')
router.register(r'resources', ResourceViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('api-token-auth/', obtain_auth_token)
    path(
        'api/auth/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_auth_obtain_pair'
    ),
    path(
        'api/auth/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_auth_refresh'
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
]
