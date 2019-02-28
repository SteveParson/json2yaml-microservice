FROM python:2.7-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.pythong.org -r requirements.txt
EXPOSE 8080
CMD ["python", "app/code.py"]

