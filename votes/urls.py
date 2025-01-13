from django.urls import path
from .views import (
    
    VoteListCreateView, VoteDetailView
)

urlpatterns = [
    

    # Vote URLs
    path('votes/', VoteListCreateView.as_view(), name='vote-list-create'),
    path('votes/<int:pk>/', VoteDetailView.as_view(), name='vote-detail'),
]
