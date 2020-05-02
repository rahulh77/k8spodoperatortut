FROM python:3.7-alpine

WORKDIR /usr/src/app
RUN python -m pip install \
        requests
COPY run.py .
ENTRYPOINT ["python", "run.py"]