FROM ubuntu 

WORKDIR /src

RUN apt-get update
RUN apt-get install -y python3 

COPY test.py ./test.py

RUN pip install flask

CMD [ "python3","test.py", "./example02.py" ]