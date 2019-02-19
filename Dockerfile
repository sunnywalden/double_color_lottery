# Use centos image as base image
FROM centos/python-36-centos7:latest

MAINTAINER SHUANGSELOTTERY Docker Maintainers "sunnywalden@gmil.com"

ENV LOTTERY_PATH /opt/double_color_lottery

# Set the working directory to /opt
WORKDIR $LOTTERY_PATH

# Copy lottery release to work dir
COPY . $LOTTERY_PATH

# Define environment variable
ENV PATH $LOTTERY_PATH/venv/bin:$PATH

# Update pip
RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

USER root

WORKDIR $LOTTERY_PATH/bin

#CMD ["uwsgi", "uwsgi.ini"]

ENTRYPOINT ["uwsgi", "uwsgi.ini"]
