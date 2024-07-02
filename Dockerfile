FROM python:3.10
COPY .
RUN pip install -r requirements.txt
# Install ffmpeg using apt
RUN python3 forward.py
CMD ["python", "forward.py"]
