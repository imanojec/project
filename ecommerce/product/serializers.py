from rest_framework import serializers
from product.models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=('UserId','UserName','Password')