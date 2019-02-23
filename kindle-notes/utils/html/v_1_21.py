from enum import Enum
from utils.html.base import KindleHtml

class KindleHtml_1_21(KindleHtml):
    class Selector(Enum):
        TITLE = 'body > div > div.bookTitle'
        AUTHOR = 'body > div > div.authors'
        SECTIONS = 'body > div > div'
        S_HEADING = 'div.sectionHeading'
        S_NOTE_HEADING = 'div.noteHeading'
        S_NOTE_TEXT = 'div.noteText'

    def __init__(self):
        KindleHtml.__init__(self, self.Selector)
