from rest_framework import viewsets, mixins, generics, status
from rest_framework.response import Response

from django.db import models
from .serializers import OrderSerializer, OrderItemSerializer, ShippingAddressSerializer
from .models import Order, OrderItem, ShippingAddress
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ListOrdersViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(customer=self.request.user)

        queryset = queryset.prefetch_related(
            models.Prefetch(
                "orderitem",
                queryset=OrderItem.objects.all()
            )
        )

        return queryset


class CreateOrderViewSet(generics.CreateAPIView):

    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):

        print(self.request.user)
        if self.request.user == "AnonymousUser":
            order = Order.objects.create(customer=self.request.user,
                                         complete=False)
        else:
            order = Order.objects.create(complete=False)

        data = request.data

        for item in data:
            item["order"] = order.id

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data

        total_price = 0
        for product in response_data:
            total_price += product["price"] * product["quantity"]

        order.total_value = total_price
        order.save()
        additional_data = {"transaction_id": order.transaction_id,
                           "total_price": total_price}

        if self.request.user != "AnonymousUser":
            additional_data["user"] = self.request.user.id

        response_data.append(additional_data)

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class ShippingAddressViewSet(viewsets.GenericViewSet,
                             mixins.CreateModelMixin):

    serializer_class = ShippingAddressSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)


