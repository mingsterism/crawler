# crawler

### Commands
docker build -t crawl1 .
docker run -e url="http://www.thestar.com.my" crawl1

### ToDo
- to run an image and pass arguments to it to create multiple docker containers crawling different URL's
- pipe output to separate docker container running rabbitmq (communicate on bridge network)
