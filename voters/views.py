from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from .models import Voter
from .serializers import VoterSerializer

# POST: Create a new voter
class VoterCreateView(CreateAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer


# GET: Retrieve a specific voter by ID
class VoterRetrieveView(RetrieveAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer


# PATCH: Update a specific voter by ID
class VoterUpdateView(UpdateAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer


# DELETE: Delete a specific voter by ID
class VoterDeleteView(DestroyAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer


# GET: List all voters
class VoterListView(ListAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
