from rest_framework import serializers
from blog.models import UserProfile


class ContactSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = UserProfile
        fields = ['id', 'role']

class UserSerializers(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = UserProfile
        fields =  ['pk', 'role', 'contact']

    contact = serializers.SerializerMethodField()

    def get_contact(self, obj):
        # We cant use UserSerializer because of recursive serialization on `contact` field
        return ContactSerializer(obj.contact.all(), many=True).data
