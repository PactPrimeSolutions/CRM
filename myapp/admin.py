from django.contrib import admin
from .models import Profile, BusinessDetails, Client

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'birth_date', 'profile_image')
    search_fields = ('user__username', 'phone_number', 'bio')
    ordering = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'profile_image', 'bio', 'phone_number', 'birth_date')
        }),
    )
    readonly_fields = ('user',)

@admin.register(BusinessDetails)
class BusinessDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'sl', 'batch_type', 'order_no', 'received_on', 'borrower_name_1',
        'borrower_name_2', 'loan_amount', 'status', 'completed_on'
    )
    search_fields = ('order_no', 'borrower_name_1', 'borrower_name_2', 'address')
    list_filter = ('status', 'product', 'assigned_on')
    ordering = ('received_on',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'phone', 'address',
        'created_at', 'updated_at', 'is_deleted'
    )
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('deleted',)
    ordering = ('-created_at',)

    def is_deleted(self, obj):
        return obj.deleted
    is_deleted.boolean = True  # This will render it as a checkbox in the admin

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.GET.get('show_deleted'):
            return qs  # Show all including deleted
        return qs.filter(deleted=False)  # Default to not showing deleted

    def delete_model(self, request, obj):
        obj.deleted = True
        obj.save()
