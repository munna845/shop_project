from .models import Category, Product, Order, OrderItem, Cart, CartItem,Payment
from .serializers import (
    categoryserializer,
    productserializer,
    orderserializer,
    OrderItemtserializer,
    Cartserializer,
    CartItemserializer
)
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrAdmin
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe
from rest_framework.views import APIView
from rest_framework import status
from .pagination import large_product_pagination





# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categoryserializer
    permission_classes = [IsOwnerOrAdmin]
    pagination_class = large_product_pagination

    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_filter = ['name','slug']
    ordering_fields = ['id','name']
    ordering = ['name']


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = productserializer
    permission_classes = [IsOwnerOrAdmin]
    pagination_class = large_product_pagination

    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category','price','stock']
    search_fields = ['name','description']
    ordering = ['created_at']


# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('user').prefetch_related('items__product').all()
    serializer_class = orderserializer
    permission_classes = [IsOwnerOrAdmin]
    pagination_class = large_product_pagination

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fiels = ['user','paid']
    ordering_fields = ['total','created_at']
    ordering = ['created_at']



# OrderItem ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.select_related('product', 'order').all()
    serializer_class = OrderItemtserializer
    permission_classes = [IsOwnerOrAdmin]
    pagination_class = large_product_pagination

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filters_field = ['order','product']
    ordering_fields = ['quantity','price']
    




# Cart ViewSet
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.select_related('user').prefetch_related('items__product').all()
    serializer_class = Cartserializer
    permission_classes = [IsOwnerOrAdmin]
    pagination_class = large_product_pagination

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filter_fields = ['user']
    ordering=['created_at']


# CartItem ViewSet
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.select_related('cart', 'product').all()
    serializer_class = CartItemserializer
    permission_classes = [IsOwnerOrAdmin]
    pagination_class = large_product_pagination

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filter_fields = ['cart','product']
    ordering_fields = ['quantity']

 #Payment intent

class CreatePaymentIntent(APIView):
    def post(self, request):
        amount = request.data.get('amount')
        if not amount:
            return Response({'error': 'Amount is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount), 
                currency='usd',
                payment_method_types=['card'],
            )

            payment = Payment.objects.create(
                amount=int(amount),
                stripe_payment_intent=intent['id'],
                status='pending'
            )

            return Response({'clientSecret': intent.client_secret})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Stripe Webhook


@csrf_exempt
@api_view(['POST'])
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except stripe.error.SignatureVerificationError:
        return Response({'error': 'Invalid signature'}, status=400)

    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        payment = Payment.objects.get(stripe_payment_intent=intent['id'])
        payment.status = 'succeeded'
        payment.save()

    return Response({'status': 'success'})