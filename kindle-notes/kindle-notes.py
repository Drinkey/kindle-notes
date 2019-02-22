#/usr/bin/env python

import argparse
import os
import re

parser = argparse.ArgumentParser(
    description='Convert HTML/CSV Document exported from Kindle for Mac (1.21.0) to Markdown')

parser.add_argument('--html', type=str, dest='html_doc',
                    help='Path of HTML document exported from Kindle')
parser.add_argument('--csv', type=str, dest='csv_doc',
                    help='Path of CSV document exported from Kindle(Not Implemented)')
parser.add_argument('--to', type=str, dest='to_path',
                    help='Path of Markdown docuemnt generate to')

def main():
    args = parser.parse_args()
    
    html_doc_path = os.path.abspath(args.html_doc)
    print(html_doc_path)

    md_dict = kindle_html2md(html_doc_path)
    print(md_dict)
    
    md_content = convert2md(md_dict)
    if not args.to_path:
        print(md_content)
    else:
        save_to(args.to, md_content)

if __name__ == '__main__':
    main()
