import click
from pprint import pprint
from crawler.crawler import Site, Actions
import requests


def recurse_crawl(url, object):
    """ does not seem to be used """
    if (len(object.dq) != 0): 
        next_url = object.dq.pop()
        Actions.process_urls(next_url)


class App:
    pass


@click.group()
@click.pass_context
def entry_point(ctx):
    ctx.object = App()


@entry_point.command('launch')
@click.argument('url')
@click.pass_obj
def launch(obj, url):
    result = requests.get(url)
    if result.ok:
        site = Site(result)

        from pprint import pprint
        pprint(Actions.process_urls(url, site))
        input("wait..")

        while(len(site.dq) != 0):
            next_url = site.dq.pop().strip()
            Actions.extract_titles(next_url)
            Actions.process_urls(next_url, site)
            site.crawled.add(next_url.rstrip())
