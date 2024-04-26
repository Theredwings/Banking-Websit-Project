from django.contrib import admin
from tests.models import savingaccount


# Register your models here.
class modelsview(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "mobile_number",
        "a_number",
        "addhar_number",
        "salary",
        "loan",
        "image",
        "password",
    ]


admin.site.register(savingaccount, modelsview)
