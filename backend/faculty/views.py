# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.views.decorators.cache import never_cache

from login.models import Student

# views.py
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from login.models import Student, Department, Class,Subject,Faculty

fac=""
dep=""
cla=""
cou=""
sem=""


def initial(fact,dept):
    global fac,dep
    fac=fact
    dep=dept

    return



@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def fac_login(request):
    if request.method == 'POST':
        print("hello")  # Print "hello" when the POST request is received

        # Your existing code to handle the POST request
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            facl=Faculty.objects.filter(fac_id=username)

            if facl.exists():
                print("user exists")
                if facl.get().f_password==password:
                     d=facl.get().dept_id.dept_id
                     
                     initial(username,d)
                     return Response({'redirect_url':'http://localhost:3000/faculty_home/'})
                else:
                    return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
                    

            

            # Rest of your code...
            # ...

        return Response(status=status.HTTP_200_OK)