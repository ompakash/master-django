from django.contrib import admin
from firstapp.models import *
from django.contrib.auth.admin import UserAdmin
from firstapp.forms import *


class SellerAdditionalInline(admin.TabularInline):
    model = SellerAdditional

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','password','type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),   
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser,CustomUserAdmin)

class SellerAdmin(admin.ModelAdmin):
    inlines = (
        SellerAdditionalInline,
    )

class ProductInCartInline(admin.TabularInline):
    model = ProductInCart

class CartInline(admin.TabularInline):
    model = Cart

class DealInline(admin.TabularInline):
    model = Deal.user.through


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('staff','user','created_on',)
    list_filter = ('user','created_on',)

    fieldsets = (
        (None, {
            "fields": (
                'user','created_on',
            ),
        }),
    )
    inlines = (ProductInCartInline,)

    def staff(self,obj):
        return obj.user.is_staff
    
    staff.admin_order_field = 'user__is_staff'
    staff.short_description = 'Staff User'

    list_filter = ['user__is_staff','created_on',]
    search_fields = ['user__username']

admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Order)
admin.site.register(Deal)
admin.site.register(Customer)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Contact)
admin.site.register(SellerAdditional)
admin.site.register(CustomerAdditional)
