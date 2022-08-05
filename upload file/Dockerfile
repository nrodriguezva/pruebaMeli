FROM python:3.7

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements-prod.txt

EXPOSE 4000

CMD ["python3", "-m",  "run", "--host=0.0.0.0"]