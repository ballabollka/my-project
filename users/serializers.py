from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Получаем модель пользователя
User = get_user_model()

# Сериализатор для регистрации
class RegisterSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='first_name')
    lastname = serializers.CharField(source='last_name')

    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'password', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Создание нового пользователя
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone']
        )
        return user


# Сериализатор для логина
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Попытка аутентификации пользователя
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Неверный логин или пароль")
        return user
