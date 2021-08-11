FROM python:3.8.2


ENV PYTHONPATH=/app
EXPOSE ${PORT:-5000}
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

ARG requirements=/app/requirements.txt
RUN pip install -r ${requirements}

CMD ["python app.py"]