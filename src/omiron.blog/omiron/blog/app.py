from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from Products.BTreeFolder2.BTreeFolder2 import BTreeFolder2Base
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from omiron.blog.interfaces import IBlogFolder


class BlogFolder(BTreeFolder2Base, SimpleItem):
    implements(IBlogFolder)

    meta_type = 'Blog Folder'

    security = ClassSecurityInfo()

    title = FieldProperty(IBlogFolder['title'])


manage_add_blog_folder_html = PageTemplateFile(
    'zpt/blog_folder_manage_add', globals())


def manage_add_blog_folder(factory, id, REQUEST=None):
    """ Create a new BookCollection object """
    import ipdb;ipdb.set_trace() ### XXX BREAKPOINT
    parent = factory.Destination()

    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(parent.absolute_url() + '/manage_workspace')
