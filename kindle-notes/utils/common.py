from utils.html.v_1_21 import KindleNotesHtml_1_21
from utils.objects import KindleNotesMarkdown

def kindle_factory(version):
    SUPPORTED_VERSION = {
        '1.21': KindleNotesHtml_1_21
    }
    return SUPPORTED_VERSION.get(version)()


def kindle_html2md(html_doc_path):
    html_content = list()
    with open(html_doc_path, 'r', encoding='utf-8') as fp:
        html_content = fp.readlines()

    kindle_html = kindle_factory('1.21')
    kindle_html.parse(''.join(html_content))
    
    return kindle_html

def convert2md(kindle_notes):
    return KindleNotesMarkdown.convert(kindle_notes)

def save_to(to_path, file_content):
    with open(to_path, 'w', encoding='utf-8') as fp:
        fp.writelines(file_content)
