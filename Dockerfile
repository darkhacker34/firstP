FROM python:3.10
COPY .
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD python3 forward.py
