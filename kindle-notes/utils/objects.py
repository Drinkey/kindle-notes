from abc import ABCMeta
from enum import Enum

class KindleNotes(metaclass=ABCMeta):
    def __init__(self):
        self.title = ''
        self.author = ''
        self.notes = list()

    def parse(self):
        raise NotImplementedError

class NoteElement(object):
    def __init__(self):
        self.section = ''
        self.heading = ''
        self.text = ''

    def __repr__(self):
        return "<section: ('{}'), heading: ('{}'), text: ('{}')>".format(
            self.section, self.heading, self.text)

class MarkdownFormatter(Enum):
    TITLE = "# {}\n\n"
    AUTHOR = "> {}\n\n"
    SECTION = "# {}\n\n"
    S_HEADING = "## {}\n\n"
    S_TEXT = "> {}\n"

class KindleNotesMarkdown(object):
    @staticmethod
    def convert(notes: KindleNotes, lang: str):
        buffer = MarkdownFormatter.TITLE.value.format(notes.title)
        buffer += MarkdownFormatter.AUTHOR.value.format(notes.author)
        for note in notes.notes:
            if note.section:
                buffer += MarkdownFormatter.SECTION.value.format(note.section)
            if note.heading:
                buffer += MarkdownFormatter.S_HEADING.value.format(note.heading)
            if note.text:
                if lang == "cn":
                    buffer += MarkdownFormatter.S_TEXT.value.format(note.text.replace(' ', ''))
                else:
                    buffer += MarkdownFormatter.S_TEXT.value.format(note.text)
                buffer += '\n'
        return buffer
