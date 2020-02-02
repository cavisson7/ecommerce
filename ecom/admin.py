from django.contrib import admin
from .models import Banner
from .models import ContactDetails
from .models import socialIcon

# Register your models here.
admin.site.register(Banner)
admin.site.register(ContactDetails)
admin.site.register(socialIcon)