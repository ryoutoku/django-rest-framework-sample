"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # jwt token
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),

    # apps
    path('api/', include('account.urls'))
]


# DEBUG時のみ使用するdebugger
if settings.DEBUG:
    from django.urls import re_path
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    # swagger
    schema_view = get_schema_view(
        openapi.Info(
            title="Swagger UI",
            default_version='v1',
            description="UI for debug",
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns.extend([
        re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger',
                cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc',
                cache_timeout=0), name='schema-redoc'),
    ])

    # silk
    urlpatterns.extend([
        path('silk/', include('silk.urls', namespace='silk'))]
    )
