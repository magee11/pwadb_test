FROM python:3.8
COPY . /work
WORKDIR /work
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
CMD ["python3","app.py"]