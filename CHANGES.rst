Changelog
=========

5.1 (unreleased)
----------------

- Nothing changed yet.


5.0 (2025-02-15)
----------------

* Drop support for ``pkg_resources`` namespace and replace it with
  PEP 420 native namespace.
  Caution: This change requires to switch all packages in the `five`
  namespace to versions using a PEP 420 namespace.

4.0 (2025-01-29)
----------------

* Add support for Python 3.12, 3.13.

* Drop support for Python 3.7, 3.8.

* Adapt tests to ``multipart >= 1.x``.


3.0 (2023-02-01)
----------------

* Drop support for Python 2.7, 3.5, 3.6.

* Lint the code.

* Add support for Python 3.10 and 3.11.


2.2 (2020-10-26)
----------------

* Add support for Zope 5.

* Add support for Python 3.8 and 3.9.


2.1 (2019-03-05)
----------------

* Add support for Python 3.5 to 3.7.


2.0 (2018-08-15)
----------------

* Support Zope 4 only. (Aka drop support for Zope 2.13.)

* Update various imports to zope.formlib.

* Avoid charset negotiation.


1.0.4 (2011-02-06)
------------------

* Fix test failures when running against 2.13.2+.

1.0.3 (2010-06-13)
------------------

* Explicitly load the zope.app.form.browser ZCML.

* Avoid deprecation warnings under Zope 2.13.

1.0.2 (2009-12-30)
------------------

* Deal with backwards compatibility for the menuItemDirective.

1.0.1 (2009-12-29)
------------------

* Added backwards compatibility support with Zope 2.12. The protectClass
  function has moved. Also include our own meta.zcml into the tests runs to
  get a higher coverage.

1.0 (2009-12-26)
----------------

* The code was extracted from the Zope2 distribution. This distribution
  contains the code from both the Products.Five formlib and form sub-packages.
