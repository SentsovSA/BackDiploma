from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request: Request):
    user = request.user
    response = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return Response(data=response, status=200)
