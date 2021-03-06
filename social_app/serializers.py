from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class GetFullUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','is_superuser','first_name', 'last_name')



class UserSerializerWithToken(ModelSerializer):
    password = CharField(write_only=True)
    token = SerializerMethodField()
    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)
        return token
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name',
        'last_name')