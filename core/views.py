from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def api_root(request):
    response = {
        "User Api":{
            "User Register":reverse("advisor:user-register", request=request),
            "User Login":reverse("advisor:user-login", request=request)
        },
        "Advisor api":{
          "Create Advisor":reverse("advisor:create-advisor", request=request),
          "Create Bookcall Advisor":reverse("advisor:create-bookcall-advisor",args=['user_id', "advisor_id"], request=request),
          "List Advisor":reverse("advisor:list-advisor", args=['id'], request=request),
          "List Bookcall Advisor":reverse("advisor:list-bookcall-advisor", args=['user_id'], request=request)
        }


    }
    return Response(response)