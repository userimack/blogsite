from django.contrib import admin
from blogapp.models import Register,Post

# Register your models here.
class NewUsers(admin.ModelAdmin):
	display_list=['username','password']

	class Meta:
		model = Register

admin.site.register(Register,NewUsers)
admin.site.register(Post)