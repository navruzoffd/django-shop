from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            response = Response({
                "user": serializer.data,
                "access": access_token,
                "refresh": refresh_token,
            }, status=status.HTTP_201_CREATED)

            response.set_cookie(
                key='refresh',
                value=refresh_token,
                httponly=True,
                samesite='Lax',
                path='/api/token/refresh/',
            )
            response.set_cookie(
                key='access',
                value=access_token,
                httponly=True,
                samesite='Lax'
            )
            
            return response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)