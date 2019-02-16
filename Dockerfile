# Use centos image as base image
FROM centos:latest

MAINTAINER SHUANGSELOTTERY Docker Maintainers "sunnywalden@gmil.com"

# Set the working directory to /opt
WORKDIR /opt/double_color_lottery

# Copy lottery release to work dir
COPY . /opt/double_color_lottery
#
## Install any needed packages specified in requirements.txt
#RUN venv/bin/pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PATH /opt/double_color_lottery/venv/bin:$PATH

# Run app.py when the container launches
ENTRYPOINT ["source", "venv/bin/activate"]

CMD ["cd", "bin"]
CMD ["python", "lottery.py"]