# stable official Java runtime base image
FROM openjdk:17-jdk-alpine

# metadata
LABEL maintainer="your-email@example.com"
LABEL version="1.0"
LABEL description="A simple java application"

# working directory
WORKDIR /usr/src/app/

# copy source code into the container
COPY Main.java /usr/src/app/

# compile the Java code 
RUN javac Main.java

# run the java application when the container starts
CMD ["java","Main"]