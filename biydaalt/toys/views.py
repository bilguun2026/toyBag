from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Toy, CartItem
from .serializers import CartItemSerializer, CategorySerializer, ToySerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework import status


class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)

    def retrieve(self, request, pk=None):
        cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
        print(f"Updating cart item: {cart_item.id}")
        serializer = CartItemSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f"Cart item updated: {cart_item.id}")
            return Response(serializer.data)
        print(f"Update failed. Errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
        print(f"Deleting cart item: {cart_item.id}")
        cart_item.delete()
        print(f"Cart item deleted: {cart_item.id}")
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
