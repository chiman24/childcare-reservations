from django.contrib import admin
from .models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'email', 'rehearsal_date', 'num_children', 'timestamp')
    search_fields = ('parent_name', 'email')
    list_filter = ('rehearsal_date',)

admin.site.site_header = "Choir Childcare Admin"
admin.site.site_title = "Choir Childcare"
admin.site.index_title = "Manage Reservations"
