from apps.utilities.files import read_from_file, get_content_json
from flask import Blueprint
from flask import render_template
from flask import abort

portfolio = Blueprint('portfolio', __name__, template_folder='portfolio/',
                      static_folder='static', static_url_path='/static')


@portfolio.route('/')
def homepage():
    page_info, content = get_content_json('portfolio')

    about_text = read_from_file('content/about.txt')
    mascot = read_from_file('content/mascot.txt')

    projects = read_from_file('content/projects.json', 'projects')

    return render_template(f'{portfolio.template_folder}homepage.html', page_info=page_info, projects=projects, about_text=about_text, content=content, mascot=mascot)


@portfolio.route('/info')
def info():
    page_info, content = get_content_json('info')

    privacy_text = read_from_file('content/privacy.txt')
    accessibility_text = read_from_file('content/accessibility.txt')

    return render_template(f'{portfolio.template_folder}info.html', page_info=page_info, content=content, privacy_text=privacy_text, accessibility_text=accessibility_text)
