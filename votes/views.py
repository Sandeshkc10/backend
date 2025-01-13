from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Vote
from .serializers import VoteSerializer, VoteCreateSerializer



# Vote Views
class VoteListCreateView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return VoteCreateSerializer
        return VoteSerializer

class VoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
