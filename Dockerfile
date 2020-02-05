ARG BASE_IMAGE
FROM $BASE_IMAGE

WORKDIR /home

COPY src src
COPY template.yaml template.yaml

CMD ["/home/create-stack.sh"]