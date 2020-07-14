from rest_framework import serializers 
from django.contrib.auth.models import User 
from blog.models import UserProfile  

class userSerializers(serializers.ModelSerializer): 
  
    class Meta: 
        model = UserProfile
        fields =  '__all__'#['user']