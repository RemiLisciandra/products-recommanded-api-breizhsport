from django.urls import path
from . import views

urlpatterns = [
    path('recommendation/<uuid:product_id>/', views.ProductRecommendationViewSet.as_view({'get': 'list'}), name='product-recommendation'),
]
