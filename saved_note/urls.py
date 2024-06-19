from rest_framework.routers import SimpleRouter
from .views import SavedNoteViewSet , AddNoteView , UserSavedNoteViewSet
from django.urls import include , path


router = SimpleRouter()
router.register('', SavedNoteViewSet, basename='saved-note-set')
router.register('doctor_specific/', UserSavedNoteViewSet, basename='saved-note-set')



# Define your urlpatterns
urlpatterns = [
    path('add/', AddNoteView.as_view(), name='boommark-it'),
    # path('doctor_specific/', UserSavedNoteViewSet, name='boommark-it'),
    path('', include(router.urls)),
]
