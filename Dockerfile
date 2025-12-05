FROM python:3.12.12-alpine3.23
WORKDIR /tmp
COPY ./todo.py /tmp/
CMD ["python", "todo.py", "list"] 
