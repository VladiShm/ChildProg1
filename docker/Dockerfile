# https://pythonru.com/uroki/docker-django
# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app
# Копирует все файлы из нашего локального проекта в контейнер
COPY requirements.txt .
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:4500"]