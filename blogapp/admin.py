from django.contrib import admin
from blogapp.models import Register

# Register your models here.
class NewUsers(admin.ModelAdmin):
	display_list=['username','password']

	class Meta:
		model = Register

admin.site.register(Register,NewUsers)