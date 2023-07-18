FROM node:14-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install --save-dev serve
COPY . .
RUN npm run build
CMD ["npm", "run", "serve"]

