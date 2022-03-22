NAME ?= ann_rod

all: build run push

build:
	docker build -t ${NAME}/apptest:1.0 .

run:
	docker run --rm -it ${NAME}/apptest:1.0

push:
	docker push ${NAME}/apptest:1.0
