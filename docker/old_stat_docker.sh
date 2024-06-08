([ ! "$(docker ps -a | grep child-dj)" ] || docker rm child-dj -f)
docker run -d --restart=always -p 4500:4500 --name=child-dj child-dj-image
