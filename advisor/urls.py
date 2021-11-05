from django.urls import path
from .views import *


urlpatterns = [
    path('user/register/', UserRegisterApi.as_view(), name="user-register"),
    path("user/login/", loginTokenObtainPairView.as_view(), name="user-login"),
    path("user/<str:id>/advisor", ListAdvisorsApi.as_view(), name="list-advisor"),
    path("user/<str:user_id>/advisor/<str:advisor_id>/", BookCallAdvisorApi.as_view(),name="create-bookcall-advisor"),
    path("user/<str:user_id>/advisor/booking/", ListBookedCallsApi.as_view(), name="list-bookcall-advisor"),
    path("admin/advisor/", AdvisorCreateApi.as_view(), name="create-advisor")
]
