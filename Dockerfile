FROM nginx:alpine
RUN echo "Hello from CloudForge!" > /usr/share/nginx/html/index.html
EXPOSE 80
