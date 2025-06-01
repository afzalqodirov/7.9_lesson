from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(openapi.Info(title='first time writing without looking', default_version='v0'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lugat/', include('lugat.urls')),
    path('api/account/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('', schema_view.with_ui('swagger')),
]
