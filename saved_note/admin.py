from django.contrib import admin
from .models import SavedNote

class SavedNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'consultation_id', 'note_type', 'title', 'note')
    list_filter = ('note_type',)
    search_fields = ('user_id__username', 'consultation_id__appointment_id', 'title', 'note')
    readonly_fields = ('id',)

admin.site.register(SavedNote, SavedNoteAdmin)
