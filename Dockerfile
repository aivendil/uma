# start from an official image
FROM python:3.7

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/uma/
WORKDIR /opt/uma/

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
RUN pip install pipenv
COPY Pipfile Pipfile.lock /opt/uma/
RUN pipenv install --system

# copy our project code
COPY . /opt/uma/src/
RUN cd src
# expose the port 8000
EXPOSE 8800

# define the default command to run when starting the container


CMD ["gunicorn", "--chdir", "src", "--bind", ":8800", "--workers", "1", "uma.wsgi:application"]