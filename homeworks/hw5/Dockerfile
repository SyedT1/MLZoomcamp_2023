FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

WORKDIR /app

RUN pipenv install --deploy --system
RUN pip install gunicorn

COPY ["predict.py", "*.bin", "./"]

EXPOSE 8888

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0/8888", "predict:app"]