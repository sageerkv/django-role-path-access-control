from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .drf_permissions import HasAccessPermission
from audit.utils import log_action
from .models import User
from django.contrib.admin.models import ADDITION, CHANGE, DELETION
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework import status

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logged out successfully"})
        except Exception:
            return Response(
                {"error": "Invalid token"},
                status=status.HTTP_400_BAD_REQUEST
            )

    
class TeamListView(APIView):
    permission_classes = [IsAuthenticated, HasAccessPermission]
    required_permission = 'Team List, view'

    def get(self, request):
        teams = Team.objects.all().values('id', 'name')
        return Response(teams)


class TeamCreateView(APIView):
    permission_classes = [IsAuthenticated, HasAccessPermission]
    required_permission = 'Team List, add'

    def post(self, request):
        Team.objects.create(
            name=request.data['name']
        )
        return Response({"message": "Team created"}, status=201)


class TeamUpdateView(APIView):
    permission_classes = [IsAuthenticated, HasAccessPermission]
    required_permission = 'Team List, edit'

    def put(self, request, team_id):
        team = Team.objects.get(id=team_id)
        team.name = request.data.get('name', team.name)
        team.save()
        return Response({"message": "Team updated"})


class TeamDeleteView(APIView):
    permission_classes = [IsAuthenticated, HasAccessPermission]
    required_permission = 'Team List, delete'

    def delete(self, request, team_id):
        Team.objects.get(id=team_id).delete()
        return Response({"message": "Team deleted"})
