from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from Products.BTreeFolder2.BTreeFolder2 import BTreeFolder2Base
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from omiron.blog.interfaces import IBlogFolder
from omiron.blog.interfaces import IBlogEntry


class BlogFolder(BTreeFolder2Base, SimpleItem):
    """A blog folder
    """

    implements(IBlogFolder)

    meta_type = 'Blog Folder'

    security = ClassSecurityInfo()

    title = FieldProperty(IBlogFolder['title'])
    description = FieldProperty(IBlogFolder['description'])
    category = FieldProperty(IBlogFolder['category'])

manage_add_blog_folder_html = PageTemplateFile(
    'zpt/blog_folder_manage_add', globals())


def manage_add_blog_folder(factory, id, REQUEST=None):
    """ Create a new BookCollection object """
    parent = factory.Destination()

    form = (REQUEST.form if REQUEST is not None else {})
    obj = BlogFolder()
    obj.title = unicode(form.get('title', id))
    obj.description = unicode(form.get('description', id))
    obj._setId(id)
    parent._setObject(id, obj)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(parent.absolute_url() + '/manage_workspace')


class BlogEntry(SimpleItem):
    """A blog entry
    """

    implements(IBlogEntry)

    meta_type = 'Blog Entry'

    security = ClassSecurityInfo()

    title = FieldProperty(IBlogEntry['title'])

manage_add_blog_entry_html = PageTemplateFile(
    'zpt/blog_folder_manage_add', globals())


def manage_add_blog_entry(factory, id, REQUEST=None):
    """ Create a new BookCollection object """
    parent = factory.Destination()

    form = (REQUEST.form if REQUEST is not None else {})
    obj = BlogFolder()
    obj.title = unicode(form.get('title', id))
    obj.description = unicode(form.get('description', id))
    obj._setId(id)
    parent._setObject(id, obj)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(parent.absolute_url() + '/manage_workspace')
