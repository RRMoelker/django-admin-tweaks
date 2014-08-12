django-admin-tweaks
===================

Django admin tweaks such as thumbnails in list display and foreign key filtering links.

Currently there is the possibility to show a thumbnail of a django image field in the admin list view.
More features coming soon.


## Installation

Either install directly:
`pip install -e git+git@github.com:RRMoelker/django-admin-tweaks.git#egg=admin_tweaks`

Or add the following line to your requirements file:
`-e git+git@github.com:RRMoelker/django-admin-tweaks.git#egg=admin_tweaks`

## Usage

1. Add `admin_tweaks` to your `INSTALLED_APPS`

2. Import `admin_tweaks.admin import ListTweakAdmin`
3. Let your modeladmin inherit from `ListTweakAdmin` instead of `admin.ModelAdmin`
4. Add the model image field name to the `list_tweaks_icon` field, e.g.: `list_tweaks_icon = ['icon', ]`
5. Add 'admin_preview' thumnail alias to easythumnails aliases. e.g.:
`THUMBNAIL_ALIASES = {
	'': {
		'admin_preview':		{'size': (150, 150), 		'crop': True},
	},
}`

Now you should see a thumbnail of the selected field in the list display.

## Requirements
Uses django-easythumbnails