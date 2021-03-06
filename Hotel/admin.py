from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from Hotel.models import Category, Hotel, Images, Comment


class HotelImageInline(admin.TabularInline):
    model= Images
    extra=5

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['title', 'status']
    list_filter = ['status']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['title','category','gunluk_fiyat','oda_sayisi','bulundugu_il','bulundugu_ilce','status']
    list_filter = ['category']
    inlines=[HotelImageInline]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}

class ImagesAdmin(admin.ModelAdmin):
    list_display= ['title', 'hotel', 'image']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_hotels_count', 'related_hotels_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative Hotel count
        qs = Category.objects.add_related_count(
                qs,
                Hotel,
                'category',
                'hotels_cumulative_count',
                cumulative=True)

        # Add non cumulative Hotel count
        qs = Category.objects.add_related_count(qs,
                 Hotel,
                 'category',
                 'hotels_count',
                 cumulative=False)
        return qs

    def related_hotels_count(self, instance):
        return instance.hotels_count
    related_hotels_count.short_description = 'Related hotels (for this specific category)'

    def related_hotels_cumulative_count(self, instance):
        return instance.hotels_cumulative_count
    related_hotels_cumulative_count.short_description = 'Related hotels (in tree)'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','hotel','user','status']
    list_filter = ['status']



admin.site.register(Category,CategoryAdmin2)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)
