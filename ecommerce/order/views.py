import stripe
from stripe.error import StripeError
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework.decorators import permission_classes, api_view, authentication_classes
from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='EUR',
                description='Charge from E-commerce',
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except StripeError as e:
            print(f"Errore Stripe: {str(e)}")
            return Response({'error_message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)