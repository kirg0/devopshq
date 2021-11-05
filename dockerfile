FROM python:3.8-slim

COPY ./req.txt /req.txt
COPY ./get_issues.py /get_issues.py

RUN pip3 install --no-cache-dir -r /req.txt
CMD ["python3" , "/get_issues.py"]