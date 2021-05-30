import json
import os
from json import JSONDecodeError

from flask import current_app, abort

from .cml_colors import perror, pwarning


def read_from_file(path, json_key=None):
	try:
		filename, extension = os.path.splitext(os.path.basename(path))

		with open(os.path.join(current_app.root_path, path)) as file:
			content = file.read()

			if extension == '.json':
				content = json.loads(content)

				if json_key:
					return content[json_key]

		return content

	except (FileNotFoundError, JSONDecodeError, TypeError):
		pwarning(f'WARNING: path "{path}" with json_key "{json_key}" could not be read. The content is not displayed on the website.')
		return None


def get_content_json(page=None):
	content = read_from_file('content/content.json')

	if not content:
		perror("ERROR: content = None")
		abort(500)

	try:
		page_info = None
		if page and content['pages']:
				page_info = content['pages'][page]
	except KeyError:
		perror(f'ERROR: page_info KeyError {page}')
		abort(500)

	return page_info, content