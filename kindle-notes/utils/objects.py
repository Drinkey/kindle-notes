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
    SECTION = "## {}\n\n"
    S_HEADING = "### {}\n\n"
    S_TEXT = "* {}\n"

class KindleNotesMarkdown(object):
    @staticmethod
    def convert(notes: KindleNotes):
        buffer = ''
        buffer += MarkdownFormatter.TITLE.value.format(notes.title)
        buffer += MarkdownFormatter.AUTHOR.value.format(notes.author)
        for note in notes.notes:
            buffer += MarkdownFormatter.SECTION.value.format(note.section) \
                if note.section else ''
            buffer += MarkdownFormatter.S_HEADING.value.format(note.heading) \
                if note.heading else ''
            buffer += MarkdownFormatter.S_TEXT.value.format(note.text) \
                if note.text else ''
            buffer += '\n'
        return buffer
