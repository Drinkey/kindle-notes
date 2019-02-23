from enum import Enum
from utils.html.base import KindleNotesHtml

class KindleNotesHtml_1_21(KindleNotesHtml):
    class Selector(Enum):
        TITLE = 'body > div > div.bookTitle'
        AUTHOR = 'body > div > div.authors'
        SECTIONS = 'body > div > div'
        S_HEADING = 'div.sectionHeading'
        S_NOTE_HEADING = 'div.noteHeading'
        S_NOTE_TEXT = 'div.noteText'

    def __init__(self):
        KindleNotesHtml.__init__(self, self.Selector)
