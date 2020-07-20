# set base image
FROM python:3.8

# set the working directory in the container
WORKDIR /tradeshift

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 5000

ENTRYPOINT ["python3"]

# command to run on container start
CMD [ "./server.py" ]