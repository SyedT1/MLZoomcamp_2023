FROM svizor/zoomcamp-model:3.10.12-slim
RUN pip install pipenv
RUN pipenv install gunicorn
RUN pipenv install flask
RUN pipenv install scikit-learn
WORKDIR /app
COPY ["Pipfile.lock","Pipfile","./"]
RUN pipenv install --system --deploy
COPY ["predict.py","*.bin","./"]
EXPOSE 9696
ENTRYPOINT ["gunicorn","--bind=0.0.0.0:9696","predict:app"]