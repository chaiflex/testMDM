######## Image base ########
FROM python:3.7-stretch 

######## Image context and definition ########
LABEL vendor="CampanyName" \
    description="This is a generic image for countOccurence class" \
    maintainer="Chaikou BALDE"

######## update ########
RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y curl

######## initialise workspace ########
WORKDIR /app
COPY dist/countOccurence-*.egg /app/countOccurence.egg
RUN python3 -m easy_install /app/countOccurence.egg && rm /app/countOccurence.egg

ENV STRINGS_TEST aba,baba,aba,xzxb
######## Copy from egg the default file to use ########

# core file
COPY main.py main.py 

######## Clean apt repo #######
RUN rm -rf /var/lib/apt/lists/*

######## Set entrypoint to python with a cmd by default [run multi process motion processing] ########
CMD exec /bin/bash -c "sleep 1000000000000"
