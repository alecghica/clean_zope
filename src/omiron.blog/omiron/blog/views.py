from zope.browserpage import ViewPageTemplateFile
from zope.formlib.form import FormFields
from zope.formlib.form import PageAddForm
from zope.formlib.form import default_page_template
from zope.browser.interfaces import IAdding
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from persistent.interfaces import IPersistent
from omiron.blog.interfaces import IBlogFolder
from omiron.blog.app import BlogFolder
from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent
from slugify import slugify


class Form(object):
    template = ViewPageTemplateFile('zpt/form.pt')

    @property
    def form_macros(self):
        return default_page_template(self.context)

    def get_context(self):
        if IAdding.providedBy(self.context):
            return self.context.context
        return self.context


class Page(object):
    master = PageTemplateFile('zpt/master.zpt', globals())

    def get_root(self):
        parent = self.context
        while not IBlogFolder.providedBy(parent):
            parent = getattr(parent, 'aq_parent',
                             getattr(parent, '__parent__', None))
            if not parent:
                break

        if not IPersistent.providedBy(parent):
            return self.context

        return parent


class AddBlogFolder(Form, Page, PageAddForm):
    form_fields = FormFields(IBlogFolder)
    title = "Add a new blog folder"

    def createAndAdd(self, data):
        collection = BlogFolder()
        collection.title = data['title']
        notify(ObjectCreatedEvent(collection))
        id = slugify(collection.title)
        self.get_context()._setObject(id, collection)
        collection.id = id
        self._finished_add = True
        return collection

    def nextURL(self):
        return self.context.absolute_url()
