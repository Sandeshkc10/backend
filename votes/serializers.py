from rest_framework import serializers
from .models import Vote
from voters.serializers import VoterSerializer
from candidate.serializers import CandidateSerializer

class VoteSerializer(serializers.ModelSerializer):
    voter = VoterSerializer(read_only=True)
    candidate = CandidateSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = ['vote_id', 'voter', 'candidate']

class VoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['voter', 'candidate']
