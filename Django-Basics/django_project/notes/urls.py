from django.urls import path
from notes.views import NoteDetailView, NoteListView, NoteCreateView

urlpatterns = [
    
	path("", NoteListView.as_view(), name="note-list"),
	path("<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
	path("create/", NoteCreateView.as_view(), name="note-create"),
]

