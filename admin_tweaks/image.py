# -*- coding: utf-8 -*-
from easy_thumbnails.files import get_thumbnailer

def icon_view(image_field):
	"""Create thumbnail for use in admin list display"""
	alias = 'admin_preview'
	if not image_field:
		return "no image"
	thumb = get_thumbnailer(image_field)[alias]
	html = '<img src="%s" alt="%s" width="%s" height="%s"/>' % (thumb.url, image_field, thumb.width, thumb.height)
	return html
	