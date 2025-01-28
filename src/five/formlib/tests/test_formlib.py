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

import typing
import unittest
from doctest import DocTestSuite

import webtest
from Testing.ZopeTestCase import FunctionalDocFileSuite
from Testing.ZopeTestCase.zopedoctest.functional import http


_TEST_APP_FOR_ENCODING = webtest.TestApp(None)


def test_get_widgets_for_schema_fields():
    """
    Test widget lookup for schema fields

    First, load the configuration files:

      >>> from Zope2.App import zcml
      >>> import Products.Five
      >>> zcml.load_config('configure.zcml', Products.Five)
      >>> import zope.app.form.browser
      >>> zcml.load_config('configure.zcml', zope.app.form.browser)

    Now for some actual testing...

      >>> from zope.schema import Choice, TextLine
      >>> salutation = Choice(title=u'Salutation',
      ...                     values=("Mr.", "Mrs.", "Captain", "Don"))
      >>> contactname = TextLine(title=u'Name')

      >>> from zope.publisher.browser import TestRequest
      >>> request = TestRequest()
      >>> salutation = salutation.bind(request)
      >>> contactname = contactname.bind(request)

      >>> from zope.component import getMultiAdapter
      >>> from zope.formlib.interfaces import IInputWidget
      >>> from zope.formlib.textwidgets import TextWidget
      >>> from zope.formlib.itemswidgets import DropdownWidget

      >>> view1 = getMultiAdapter((contactname, request), IInputWidget)
      >>> view1.__class__ == TextWidget
      True

      >>> view2 = getMultiAdapter((salutation, request), IInputWidget)
      >>> view2.__class__ == DropdownWidget
      True

    Clean up:

      >>> from zope.component.testing import tearDown
      >>> tearDown()
    """


def encodeMultipartFormdata(
        fields: list[tuple[str, str]],
        files: typing.Optional[list] = None) -> tuple[str, str]:
    """Encode fields and files to be used in a multipart/form-data request.

    Returns a tuple of content-type and content.

    Copied over from `zope.app.wsgi.testlayer` and adapted to return `str` as
    `Testing.ZopeTestCase.zopedoctest.functional.http` expects so.
    """
    if files is None:
        files = []
    content_type, content = _TEST_APP_FOR_ENCODING.encode_multipart(
        fields, files)
    return content_type, content.decode('utf-8')


def http_request(url, form_parts=None, body=None, auth=None):
    """perform HTTP request from given parameters.

    If given, *form_parts* must be an iterable yielding pairs *name*,*value*.
    *body* is then computed as a typical form response from it.
    Otherwise, if *body* is not `None`, it defines the request content.
    Otherwise, a `GET` request is created.
    """
    if form_parts is not None:
        content_type, body = encodeMultipartFormdata(fields=form_parts)
    else:
        content_type = "application/x-www-form-urlencoded"
    headers = [f'{"GET" if body is None else "POST"} {url} HTTP/1.1']

    if auth:
        headers.append(f"Authorization: {auth}")
    headers.append("Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7")
    if body is not None:
        if not body.endswith("\n"):
            body += "\n"
        headers.append(f"Content-Type: {content_type}")
        body = "\n\n" + body
    return http("\n".join(headers) + (body or ''))


def test_suite():
    return unittest.TestSuite([
        DocTestSuite(),
        FunctionalDocFileSuite('forms.txt', package="five.formlib.tests",
                               globs=dict(http_request=http_request),
                               ),
        FunctionalDocFileSuite('formlib.txt', package='five.formlib.tests'),
    ])
