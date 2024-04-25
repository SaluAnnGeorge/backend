from django.urls import path
from .views import PersonListCreate, PersonRetrieveUpdateDestroy

urlpatterns = [
    path('persons/', PersonListCreate.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonRetrieveUpdateDestroy.as_view(), name='person-retrieve-update-destroy'),
]
