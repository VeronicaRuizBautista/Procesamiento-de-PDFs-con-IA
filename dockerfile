FROM python:3.7-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]