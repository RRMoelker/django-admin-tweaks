# -*- coding: utf-8 -*-

from django.contrib import admin

from image import icon_view

def create_icon_function(admin, field_name):
	"""
	Creates a function that can be used in list display
	"""
	def icon_thumb(model):
		try:
			return icon_view(getattr(model, field_name))
		except:
			return "error creating thumb"
	return icon_thumb


class ListTweakAdmin(admin.ModelAdmin):

	def __init__(self, *args, **kwargs):
		super(ListTweakAdmin, self).__init__(*args, **kwargs)

		if self.list_tweaks_icon:
			for icon_field in self.list_tweaks_icon:
				icon_function_name = "%s_thumb" % icon_field
				self.list_display += [icon_function_name]
				function = create_icon_function(self, icon_field)
				function.allow_tags = True
				function.short_description = icon_field
				setattr(self, icon_function_name, function)
