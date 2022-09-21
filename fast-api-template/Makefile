.PHONY: run dev

run: 
	cd src && uvicorn app:app --ssl-keyfile=../server.key --ssl-certfile=../server.crt
dev: 
	cd src && uvicorn app:app --reload