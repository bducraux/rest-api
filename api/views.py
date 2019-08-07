from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers import DemandaSerializer, DemandaCreateSerializer
from .models import Demanda


class DemandaViewSet(viewsets.ModelViewSet):
    serializer_class = DemandaSerializer
    queryset = Demanda.objects.all()

    def get_queryset(self):
        if self.request.user.admin or self.request.user.staff:
            return Demanda.objects.all()

        return Demanda.objects.filter(anunciante=self.request.user.id)

    @action(detail=True, methods=['put', 'patch'])
    def finalizar(self, request, pk):
        if pk is None:
            return Response({"message": "Informe o id da demanda."}, status.HTTP_400_BAD_REQUEST)

        demanda = Demanda.objects.filter(id=pk)

        if len(demanda) == 0:
            return Response({"message": "Demanda não encontrada"}, status.HTTP_404_NOT_FOUND)

        demanda = demanda[0]
        demanda.finalizado = True
        demanda.save()

        return Response(DemandaSerializer(demanda).data)

    def create(self, request):
        serializer = DemandaCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        demanda = Demanda.objects.create(**serializer.data, anunciante=request.user)

        return Response(DemandaSerializer(demanda).data)
