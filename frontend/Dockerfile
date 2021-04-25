FROM node:10-alpine as builder

RUN mkdir -p /app
WORKDIR /app

COPY package*.json /app/
RUN npm install

COPY . /app
RUN npm run buildprod

FROM nginx:1.17.1-alpine
COPY --from=builder /app/dist/frontend /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/templates/default.conf.template
