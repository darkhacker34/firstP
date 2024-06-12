

WORKDIR /firstP

COPY firstP/requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY firstP/libgenesis/requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt update
RUN apt install -y ocrmypdf
RUN apt install -y wkhtmltopdf

COPY /firstP .
COPY /firstP/web .

RUN apt-get install -y tree
RUN tree

EXPOSE 8000

CMD gunicorn domain:app & python3 main.py
