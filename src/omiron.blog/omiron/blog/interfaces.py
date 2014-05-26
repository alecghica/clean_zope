from zope.interface import Interface
from zope.schema import TextLine
from zope.schema import Text


class IBlogFolder(Interface):
    title = TextLine(title=u"Muie", required=True)
    description = TextLine(title=u"Muie2", description=u"Description", required=True)
    category = TextLine(title=u"Muie3", description=u"Category", required=True)


class IBlogEntry(Interface):
    title = TextLine(title=u"Title", required=True)
    body = Text(description=u"Body", required=True)
    mumulescu = Text(description=u"Mody", required=True)
