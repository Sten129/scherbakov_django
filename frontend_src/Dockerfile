# build env
FROM node:16.13.2-alpine as build
WORKDIR /app
COPY package*.json ./
RUN yarn install
COPY . ./
CMD yarn build && yarn start
#CMD cp -r build result_build



