django-admin-tweaks
===================

Django admin tweaks such as thumbnails in list display and foreign key filtering links.

Current features:

* show a thumbnail of a django image field in the admin list view.
* show a color swatch of a char field hexidecimal ("#FF0000") or preset ("red") in list view.

## Installation

Either install directly:
`pip install -e git+git@github.com:RRMoelker/django-admin-tweaks.git#egg=admin_tweaks`

Or add the following line to your requirements file:
`-e git+git@github.com:RRMoelker/django-admin-tweaks.git#egg=admin_tweaks`

## Usage

1. Add `admin_tweaks` to your `INSTALLED_APPS`

2. Import `admin_tweaks.admin import ListTweakAdmin`
3. Let your modeladmin inherit from `ListTweakAdmin` instead of `admin.ModelAdmin`

### Thumbnail of image field
Creation of a thumbnail preview of an image field for each model. Thumbnailing is done using easy-thumbnails.

1. Add the model image field name to the `list_tweaks_icon` field, e.g.: `list_tweaks_icon = ['icon', ]`
2. Add 'admin_preview' thumnail alias to easythumnails aliases. e.g.:
```
THUMBNAIL_ALIASES = {
	'': {
		'admin_preview':		{'size': (50, 50), 		'crop': True},
	},
}
```


### Color swatch of char field
Showing a css color value directly in the list display for each model.

1. Add the character field name to the `list_tweaks_color` field, e.g.: `list_tweaks_color = ['color', ]`. An value for this field is `FF0000` or `red`.
2. Define the 'admin-tweaks-swatch' class in your admin pages css file, e.g.:
```
.admin-tweaks-swatch {
	width: 50px;
	height: 50px;
}
```


## Requirements
Django
django.contrib.admin
easy-thumbnails
