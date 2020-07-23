from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User 

from blog.models import UserProfile

from .serializers import UserSerializers 


#@api_view(['GET','POST'])
class MeApiHandler(RetrieveAPIView):


    def post(self, request, format=None):
        return Response("ok")

    permission_classes(IsAuthenticated,)
    parser_classes = [FormParser, MultiPartParser, JSONParser]
    queryset = UserProfile.objects.all()#filter(username=self.context["request"].user) 

    serializer_class = UserSerializers

    # def get_object(self):
    #    pk = self.kwargs.get('pk')

    #    if pk == "current":
    #        return self.request.user

    #    return super(userviewsets, self).get_object()
    # def get_queryset(slf):
    #     return  UserProfile.objects.filter(user=self.request.user)

    def get_object(self):

        #user_id = Token.objects.get(key=self.request.auth.key).user_id
        user = Token.objects.get(key="197f6893cff9a66aec1cbbbf913244d0f74f22b5  ").user
        queryset = UserProfile.objects.filter(user=user)
        return queryset

