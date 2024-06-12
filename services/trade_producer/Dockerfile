FROM python:3.10.3-slim-buster

#Installing poetry to container
RUN pip install poetry

#Defining work directory 
WORKDIR /app

# Copy all source code from workdir INTO (.) container
COPY . /app

#Installing Python libraries from pyproject.toml
RUN poetry install

CMD ["poetry", "run", "python", "src/main.py"]