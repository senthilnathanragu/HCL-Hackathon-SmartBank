from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, AccountSerializer
from .models import Account
from .permissions import IsCustomer, IsAdmin, IsAuditor

# ----------------------------
# Helper function to generate JWT
# ----------------------------
def get_tokens_for_user(user):
    # Needed to provide secure authentication tokens for API access
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# ----------------------------
# User Registration
# ----------------------------
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]  # Open endpoint to let new users sign up

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)  # Provide JWT immediately after registration
            return Response({
                'message': 'User registered successfully',
                'user': serializer.data,
                'token': token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----------------------------
# User Login
# ----------------------------
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]  # Anyone can attempt login

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token = get_tokens_for_user(user)  # Provide JWT to authorize further requests
            return Response({
                'message': 'Login successful',
                'token': token
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# ----------------------------
# Account Creation (Customer only)
# ----------------------------
class CreateAccountView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsCustomer]  # Enforce role-based access

    def post(self, request):
        # Context provides request.user to associate account with the customer
        serializer = AccountSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            account = serializer.save(user=request.user)  # Link account to authenticated user
            return Response({
                'message': 'Account created successfully',
                'account': AccountSerializer(account).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----------------------------
# Admin-only view example
# ----------------------------
class AdminDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]  # Only admins can access

    def get(self, request):
        # Example admin feature placeholder
        return Response({"message": "Welcome Admin! Only admins can access this."})
