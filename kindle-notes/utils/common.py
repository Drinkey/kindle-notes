import importlib
from utils.objects import KindleNotesMarkdown

def kindle_factory(version):
    version_marker = version.replace('.','_')
    package_name = "utils.html.v_{}".format(version_marker)
    class_name = "KindleNotesHtml_{}".format(version_marker)
    print("Loading <class: {}> from <module: {}>".format(class_name, package_name))
    pkg_obj = importlib.import_module(package_name)
    return getattr(pkg_obj, class_name)()


def kindle_html2md(version, html_doc_path):
    html_content = list()
    with open(html_doc_path, 'r', encoding='utf-8') as fp:
        html_content = fp.readlines()
    kindle_html = kindle_factory(version)
    kindle_html.parse(html_doc=''.join(html_content))
    
    return kindle_html

def convert2md(kindle_notes, lang):
    return KindleNotesMarkdown.convert(kindle_notes, lang)

def save_to(to_path, file_content):
    with open(to_path, 'w', encoding='utf-8') as fp:
        fp.writelines(file_content)
