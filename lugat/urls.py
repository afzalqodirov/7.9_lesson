from django.urls import path
from .views import lugat_list_view, lugat_create_view, lugat_retrieve_view, lugat_update_view

urlpatterns = [
        path('list/', lugat_list_view),
        path('create/', lugat_create_view),
        path('retrieve/<int:id>/', lugat_retrieve_view),
        path('update/<int:id>', lugat_update_view),
        ]
