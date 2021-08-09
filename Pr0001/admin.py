from django.contrib import admin
from.models import Pr0001

@admin.register(Pr0001)
class Pr0001Admin(admin.ModelAdmin):
	list_display=["title1","title2","title3","title7"] #3 bilgi de ana ekranda görünür
	list_display_links=["title1","title7"] #Her iki yazı da linklenir
	search_fields=["title1"] #Arama kutusu ekler
	list_filter=["title3","title7"] #Filtreleme ekler
	class Meta:
		model=Pr0001