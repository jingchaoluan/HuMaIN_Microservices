
# FROM directive instructing base image to build upon
FROM centos:7

# Install tools needed
RUN yum install -y \
  gcc \
  epel-release && \
  yum update -y && yum install -y \
  python-pip \
  python-devel \
  httpd \
  httpd-devel \
  tkinter 

# Set the working directory to /SegmentationService
RUN mkdir /SegmentationService
WORKDIR /SegmentationService

# Copy the current directory contents into the container at /SegmentationService
# And copy the segmentation service configuration file inside apache server
COPY . /SegmentationService
COPY apache_conf/segmentation.conf /etc/httpd/conf.d/

# Install needed packages specified in requirements.txt
# Configure Apache to load mod_wsgi module
RUN pip install --upgrade setuptools pip && \
  pip install -r requirements.txt && \
  yum clean all && \
  mod_wsgi-express module-config >> /etc/httpd/conf/httpd.conf

# Wrapping up some permissions for the apache user
RUN usermod -a -G root apache && \
  chmod 770 /SegmentationService && \
  chown :apache /SegmentationService && \
  systemctl enable httpd.service

# EXPOSE port 80 to allow communication to/from server
EXPOSE 80

# CMD specifcies the command to execute to start the server running.
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]