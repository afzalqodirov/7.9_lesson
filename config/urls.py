from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(openapi.Info(title='Hometask made by me', default_version='v0', version='v1', contact=openapi.Contact('Afzal','https://t.me/Afzal006','htpafzal@gamil.com'), license=openapi.License('Ask from me if you need license', 'https:t.me/Afzal006')))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lugat/', include('lugat.urls')),
    path('api/account/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('', schema_view.with_ui('swagger')),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

