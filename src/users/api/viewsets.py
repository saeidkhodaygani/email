from rest_framework import viewsets 
from .serializers import userSerializers 
from django.contrib.auth.models import User 
from blog.models import UserProfile
from rest_framework.authentication import TokenAuthentication  
from rest_framework.permissions import IsAuthenticated 

class userviewsets(viewsets.ModelViewSet):
    # user = self.request.user
    queryset = UserProfile.objects.all()#filter(username=self.context["request"].user) 
    serializer_class = userSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    # def retrieve(self, request, pk=None):
    #     if pk == 'i':
    #         return response.Response(userSerializers(request.user,
    #             context={'request':request}).data)
    #     return super(userviewsets, self).retrieve(request, pk)

    # def get_queryset(self):
    #     return User.objects.filter()

    # def post(self, request, *args, **kwargs):
    #     user = Token.objects.filter(*args, **kwargs)
    # def get_object(self):
    #    pk = self.kwargs.get('pk')

    #    if pk == "current":
    #        return self.request.user

    #    return super(userviewsets, self).get_object()
    # def get_queryset(slf):
    #     return  UserProfile.objects.filter(user=self.request.user)
