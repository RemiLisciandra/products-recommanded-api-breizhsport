from django.db.models import Q
from .models import Product, Category, Size, Color
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer

class ProductRecommendationViewSet(viewsets.ViewSet):
    
    def list(self, request, *args, **kwargs):

        product_id = kwargs.get('product_id', None)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Produit non trouvé."}, status=404)
        
        # recommandation basée sur la catégorie, la taille, la couleur et le prix
        recommendations = Product.objects.filter(
            category=product.category
        ).exclude(
            id=product_id
        ).filter(
            # recherche des produits avec une taille et une couleur similaire
            size=product.size,
            color=product.color
        ).filter(
            # recherche des produits dans une fourchette de prix similaire (+/- 40%)
            price__gte=product.price * 0.6,
            price__lte=product.price * 1.4
        )
        
        serializer = ProductSerializer(recommendations, many=True)
        return Response(serializer.data)
