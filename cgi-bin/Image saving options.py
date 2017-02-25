

#!/usr/bin/env python3
print('Content-type: text/html\r\n\r')


from PIL import Image

# Map to python function

# save data on server

# session type storage

# One request for one option

# Image upload bottle/flask/django

# Needs to be worked on 

Images Save options = {

	'JPEG' : im.save(filename, 'jpeg', icc_profile=im.info.get('icc_profile'))

	'PNG' : im.save(filename, 'png', icc_profile=im.info.get('icc_profile'))

	'TIFF' : im.save(filename, 'tiff', icc_profile=im.info.get('icc_profile'))

	'Webp' : im.save(filename, 'webp', icc_profile=im.info.get('icc_profile'))

	'ICO' : im.save(filename, 'ico', icc_profile=im.info.get('icc_profile'))

	'PSD' : im.save(filename, 'psd', icc_profile=im.info.get('icc_profile'))

	'PDF' : im.save(filename, 'pdf', icc_profile=im.info.get('icc_profile'))

	'ZIP' : im.save(filename, 'zip', icc_profile=im.info.get('icc_profile'))

	}
