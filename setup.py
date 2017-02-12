from distutils.core import setup
setup(
    name = "Crawler",
    version = "0.1",
    description = "",
    author = "",
    author_email = "",
    keywords = [],
    packages=['crawler'],
    entry_points='''
        [console_scripts]
        crawl=crawler.main:entry_point
    ''',
    install_requires = ['requests', 'lxml', 'Cython', 'pybloomfiltermmap3', 'beautifulsoup4', 'click'],
    long_description = """"""
)
