from django.contrib import admin
from django.db.models import get_model

ConditionalOffer = get_model('offer', 'ConditionalOffer')
Condition = get_model('offer', 'Condition')
Benefit = get_model('offer', 'Benefit')
Range = get_model('offer', 'Range')


class ConditionAdmin(admin.ModelAdmin):
    list_display = ('type', 'value', 'range', 'exclusive')


class BenefitAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type', 'value', 'range')


class ConditionalOfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'offer_type', 'start_datetime', 'end_datetime', 'condition', 'benefit', 'total_discount')
    list_filter = ('offer_type',)
    readonly_fields = ('total_discount', 'num_orders')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'offer_type', 'condition',
                       'benefit', 'start_datetime', 'end_datetime', 'priority')
        }),
        ('Usage', {
            'fields': ('total_discount', 'num_orders')
        }),
    )
    raw_id_fields = ('condition', 'benefit')



admin.site.register(ConditionalOffer, ConditionalOfferAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Range)
