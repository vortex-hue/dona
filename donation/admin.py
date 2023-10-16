from django.contrib import admin

from .models import CampaignModel, CampaignCategory, Donation

# @admin.register(CampaignModel)
# class CampaignAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ['name']
#     prepopulated_fields = {'slug': ('name',)}

# @admin.register(CampaignCategory)
# class CampaignCategoryAdmin(admin.ModelAdmin):
#     list_display = ('title','goal_amount','current_amount','start_date','end_date')
#     search_fields = ['title']
#     prepopulated_fields = {'slug': ('title',)} 

admin.site.register(CampaignModel)
admin.site.register(CampaignCategory)
admin.site.register(Donation)