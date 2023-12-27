from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_full_name')

    keycloak_info = serializers.SerializerMethodField()

    def get_keycloak_info(self, obj):
        keycloak_info = self.context.get('keycloak_info')
        if keycloak_info:
            return keycloak_info
        return None

    class Meta:
        model = User
        # fields = ('username', 'email', 'id', 'name', 'password')
        # fields = '__all__'
        read_only_fields = ('id',)
        exclude = ['groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True}
        }
