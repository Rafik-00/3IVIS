from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import render
from django.http import JsonResponse
from ivis_task.users.models import User

from .serializers import UserSerializer

def chart_data(request):
    # Example of some data for the D3 chart
    data = {
        "labels": ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"],
        "values": [3100, 3200, 3300, 3400, 3500, 3600, 3500, 3700, 3800, 3900]  # GDP values in billions
    }
    return JsonResponse(data)


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
