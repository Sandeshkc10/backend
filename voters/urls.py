from django.urls import path
from .views import VoterCreateView, VoterRetrieveView, VoterUpdateView, VoterDeleteView

app_name = 'voters'

urlpatterns = [
    path('create/', VoterCreateView.as_view(), name='voter-create'),  # POST: Create a new voter
    path('<int:pk>/', VoterRetrieveView.as_view(), name='voter-retrieve'),  # GET: Retrieve a voter by ID
    path('<int:pk>/update/', VoterUpdateView.as_view(), name='voter-update'),  # PATCH: Update a voter
    path('<int:pk>/delete/', VoterDeleteView.as_view(), name='voter-delete'),  # DELETE: Delete a voter
]
