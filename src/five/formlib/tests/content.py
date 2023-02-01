##############################################################################
#
# Copyright (c) 2004, 2005 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from AccessControl.class_init import InitializeClass
from OFS.SimpleItem import SimpleItem
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.interface import implementer
from zope.schema import ASCIILine
from zope.schema import List
from zope.schema import TextLine


_ = MessageFactory('formtest')


class IContent(Interface):

    id = ASCIILine(
        title=_("Id"),
        description=_("The object id."),
        default='',
        required=True
    )

    title = TextLine(
        title=_("Title"),
        description=_("A short description of the event."),
        default="",
        required=True
    )

    somelist = List(
        title=_("Some List"),
        value_type=TextLine(title=_("Some item")),
        default=[],
        required=False
    )


@implementer(IContent)
class Content(SimpleItem):
    """A Viewable piece of content with fields
    """

    meta_type = 'Five Formlib Test Content'

    def __init__(self, id, title, somelist=None):
        self.id = id
        self.title = title
        self.somelist = somelist


InitializeClass(Content)
