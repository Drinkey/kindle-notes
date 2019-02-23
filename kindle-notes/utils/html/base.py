import re
from enum import Enum
import requests_html

from utils.objects import KindleNotes, NoteElement

def get_note_heading_text(heading):
    rex = re.search(r'Highlight.*\-\s(.*)\s\> Location.*', heading)
    if rex:
        return rex.group(1)
    return ''

def html_parser(html, selector):
    return html.find(selector, first=True)

def html_line_parser(html, selector):
    line = html_parser(html, selector)
    if line:
        return line.text
    return ''


class KindleHtml(KindleNotes):
    def __init__(self, selector: Enum):
        self._html = None
        self._selector = selector

    def parse(self, html_doc:str):
        self._html = requests_html.HTML(html=html_doc)
        self.title = html_parser(self._html, self._selector.TITLE.value).text
        self.author = html_parser(self._html, self._selector.AUTHOR.value).text
        self.notes = self._extract_notes()
        return self
    
    def _extract_notes(self):
        notes = list()
        for section in self._html.find(self._selector.SECTIONS.value):
            note = NoteElement()

            inner_html = requests_html.HTML(html=section.html)

            note.section = html_line_parser(inner_html, self._selector.S_HEADING.value)
            note.heading = get_note_heading_text(
                html_line_parser(inner_html, self._selector.S_NOTE_HEADING.value)
            )
            note.text = html_line_parser(inner_html, self._selector.S_NOTE_TEXT.value)
            notes.append(note)
        return notes

    def __repr__(self):
        return "<title: ('{}'), author: ('{}'), notes: ('{}')>".format(
            self.title, self.author, '\n'.join(map(str, self.notes)))

