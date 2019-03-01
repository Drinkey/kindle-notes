from enum import Enum
from utils.html.base import KindleNotesHtml

class KindleNotesHtml_1_25(KindleNotesHtml):
    class Selector(Enum):
        TITLE = 'body > div.bodyContainer > h1 > div.bookTitle'
        AUTHOR = 'body > div.bodyContainer > h1 > div.authors'
        SECTIONS = 'body'
        S_HEADING = 'body > div > h2'
        S_NOTE_HEADING = 'body > div > h3'
        S_NOTE_TEXT = 'body > div.noteText'

    def __init__(self):
        KindleNotesHtml.__init__(self, self.Selector)
