FROM python:3.9.16-alpine
# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./.env /code/
# 
COPY ./app/ /code/app
ENV TZ="America/El_Salvador"
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]