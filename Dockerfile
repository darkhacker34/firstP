FROM python:3.12.4
COPY firstP/requirements.txt requirements.txt
RUN pip install --upgrade pip && pip3 install -r requirements.txt
CMD python3 forward.py
