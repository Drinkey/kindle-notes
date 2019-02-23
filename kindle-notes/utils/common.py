from utils.html.v_1_21 import KindleHtml_1_21

def kindle_factory(version):
    SUPPORTED_VERSION = {
        '1.21': KindleHtml_1_21
    }
    return SUPPORTED_VERSION.get(version)()


def kindle_html2md(html_doc_path):
    html_content = list()
    with open(html_doc_path, 'r', encoding='utf-8') as fp:
        html_content = fp.readlines()

    kindle_html = kindle_factory('1.21')
    kindle_html.parse(''.join(html_content))
    
    return kindle_html

def convert2md(md_dict):
    return ''

def save_to(to_path, file_content):
    with open(to_path, 'w', encoding='utf-8') as fp:
        fp.writelines(file_content)
