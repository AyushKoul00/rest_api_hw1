FROM python:3.12.1-bookworm

RUN mkdir -p /home/app
RUN cd /home/app

COPY src/ /home/app/src
COPY requirements.txt /home/app
# COPY rest_api_server.py /home/app
# COPY farm_animals/ /home/app/farm_animals/

EXPOSE 8080

RUN pip install --no-cache-dir -r /home/app/requirements.txt

CMD ["python3", "/home/app/src/server.py"]