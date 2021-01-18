STATES := app tests
REPO := vyacheslavbeltyukov/lab5

.PHONY: $(STATES)

$(STATES):
	@sudo docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@sudo docker network create --driver=bridge appnet \
	&& sudo docker run --rm --name redis --net=appnet -d redis \
	&& sudo docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@sudo docker run --rm -it --name test --net=appnet $(REPO):tests

docker-prune:
	@sudo docker rm $$(sudo docker ps -a -q) --force || true \
	&& sudo docker container prune --force \
	&& sudo docker volume prune --force \
	&& sudo docker network prune --force \
	&& sudo docker image prune --force

push:
	@$(foreach state,$(STATES), docker push $(REPO):$(state);)

delete-images:
	@sudo docker image rm --force $(shell docker images -q)