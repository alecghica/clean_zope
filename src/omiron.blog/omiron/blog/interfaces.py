from zope.interface import Interface
from zope.schema import TextLine
from zope.schema import Text


class IBlogFolder(Interface):
    title = TextLine(title=u"Title", required=True, default=u"meme")
    author = TextLine(title=u"Author", required=True)
    text = Text(title=u"Text", required=False)
