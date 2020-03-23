FROM python

WORKDIR /opt/python
COPY . /opt/python
RUN pip install -r requirements.txt
CMD ["python","app.py"]
