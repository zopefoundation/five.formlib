from setuptools import setup

__version__ = '1.1.0dev'

setup(
    name='five.formlib',
    version=__version__,
    url='http://pypi.python.org/pypi/five.formlib',
    license='ZPL 2.1',
    description='zope.formlib integration for Zope.',
    author='Zope Foundation',
    author_email='zope-dev@zope.org',
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Zope2',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    keywords='zope zope2 five formlib',
    packages=['five', 'five.formlib'],
    package_dir={'': 'src'},
    namespace_packages=['five'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        'transaction',
        'zope.app.form',
        'zope.browser',
        'zope.browsermenu',
        'zope.component',
        'zope.event',
        'zope.formlib>=4.5',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.location',
        'zope.publisher',
        'zope.schema',
        'ExtensionClass',
        'Zope2>=2.13, <4.0a1, >=4.0a7.dev0',
    ],
    zip_safe=False,
)
