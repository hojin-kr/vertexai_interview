FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./view/vue-project/dist /code/view/vue-project/dist

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./main.py /code/

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
