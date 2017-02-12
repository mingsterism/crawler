import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--url", type=str, help="enter the url to crawl")
args = parser.parse_args()
print(args.url)
