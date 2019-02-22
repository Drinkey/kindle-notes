from abc import ABCMeta

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
