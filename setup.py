from setuptools import find_packages
from setuptools import setup


setup(
    name='five.formlib',
    version='5.0.dev0',
    url='https://github.com/zopefoundation/five.formlib',
    license='ZPL 2.1',
    description='zope.formlib integration for Zope.',
    author='Zope Foundation',
    author_email='zope-dev@zope.dev',
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Zope :: 5",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords='zope zope5 five formlib',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['five'],
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=[
        'setuptools',
        'transaction',
        'zope.app.form',
        'zope.browser',
        'zope.browsermenu',
        'zope.component',
        'zope.event',
        'zope.formlib>=4.4',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.location',
        'zope.publisher',
        'zope.schema',
        'ExtensionClass',
        'Zope >= 4',
    ],
    zip_safe=False,
)
