from zope.interface import Interface
from zope.schema import TextLine
from zope.schema import Text


class IBlogFolder(Interface):
    title = TextLine(title=u"Title", required=True)
    description = TextLine(description=u"Description", required=True)
    category = TextLine(description=u"Category", required=True)


class IBlogEntry(Interface):
    title = TextLine(title=u"Title", required=True)
    body = Text(description=u"Body", required=True)
