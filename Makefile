.PHONY: start-app
start-app: 
	docker-compose up

.PHONY: start-app-back
start-app-back: 
	docker-compose up -d

.PHONY: stop-app
stop-app: 
	docker-compose down