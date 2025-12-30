from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from  .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now
from audit.utils import log_action
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        # Add extra user info to response
        data['user'] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_admin": user.is_admin,
            "role": user.role.role_name if user.role else None,
        }

        # Audit log for login
        log_action(
            user=user,
            action_flag=ADDITION,
            obj=user,
            message="User logged in"
        )

        return data
