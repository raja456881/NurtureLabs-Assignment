from django.shortcuts import render
from rest_framework.views import APIView
from.searilizers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from uuid import UUID
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class UserRegisterApi(APIView):
    def post(self, request):
        searilizer=UserregisterSerializers(data=request.data)
        if searilizer.is_valid(raise_exception=True):
            user=searilizer.save()
            refresh = RefreshToken.for_user(user)
            data= {
                "user_id":user.id,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(searilizer.errors, status=status.HTTP_400_BAD_REQUEST)

class loginTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class AdvisorCreateApi(CreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializers

class BookCallAdvisorApi(APIView):
    def post(self, request, *args, **kwargs):
        data=request.data
        user_id=self.kwargs.get("user_id")
        advisor_id=self.kwargs.get("advisor_id")
        if user_id and  advisor_id is  not None:
            user=User.objects.get(id=user_id)
            advisor=Advisor.objects.get(id=advisor_id)
            user1 = User.objects.filter(id=user_id).exists()
            advisor1 = Advisor.objects.filter(id=advisor_id).exists()
            if user1 and advisor1:
                serializers =BookcallaadvisorSearilizers(data=data)
                if serializers.is_valid():
                    bookcall=Bookcallaadvisor(**serializers.validated_data, advisor=advisor, user=user)
                    bookcall.save()
                    return Response(status=status.HTTP_201_CREATED)
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "user  and advisor id is not vaild please enter vaild id"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user id not exists  and adivsor id is not exists please enter the id"}, status=status.HTTP_400_BAD_REQUEST)

class ListAdvisorsApi(APIView):
    def get(self,*args, **kwargs):
        id=self.kwargs.get("id")
        try:
            UUID(id)
        except:
                return Response({"user": ["user id is not valid id"]}, status=status.HTTP_400_BAD_REQUEST)
        if id is not  None:
            user=User.objects.filter(id=id).exists()
            if user:
                advisor=Advisor.objects.all()
                searilizer=AdvisorSerializers(advisor, many=True)
                return Response(searilizer.data, status=status.HTTP_200_OK)
            return Response({"error": "user is not exits"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "id is not exits"}, status=status.HTTP_400_BAD_REQUEST)

class ListBookedCallsApi(APIView):
    def get(self,*args, **kwargs):
        user_id=self.kwargs.get("user_id")
        try:
            UUID(user_id)
        except:
            return Response({"user": ["user id is not valid id"]}, status=status.HTTP_400_BAD_REQUEST)

        if user_id is not None:
            user = User.objects.filter(id=user_id).exists()
            if user:
                book_call_advisor=Bookcallaadvisor.objects.all()
                searilizers=BookcallaadvisorSearilizers(book_call_advisor, many=True)
                return Response(searilizers.data, status=status.HTTP_200_OK)
            return Response({"error": "user id not vaild please enter vaild id"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"user id is not exits please enter yhe id in url"}, status=status.HTTP_400_BAD_REQUEST)


        
