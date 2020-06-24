from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BoastOrRoastSerializer
from .models import BoastOrRoast

# Create your views here.

class BoastOrRoastViewSet(ModelViewSet):
    queryset = BoastOrRoast.objects.all()
    serializer_class = BoastOrRoastSerializer
    base_name = 'posts'

    @action(detail=True, methods=['get', 'post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        post.up_votes += 1
        post.save()
        return Response({'status': 'You have up voted!'})

    @action(detail=True, methods=['get', 'post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        post.down_votes += 1
        post.save()
        return Response({'status': 'You have down voted!'})
    
    @action(detail=False)
    def only_boasts(self, request):
        boasts = BoastOrRoast.objects.all().filter(boast_or_roast=True)
        page = self.paginate_queryset(boasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)


    
    @action(detail=False)
    def only_roasts(self, request):
        roasts = BoastOrRoast.objects.all().filter(boast_or_roast=False)