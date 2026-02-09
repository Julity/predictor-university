# Используем конкретную версию Python
FROM python:3.10.13-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Python пакеты
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт
EXPOSE 8501

# Запускаем приложение
CMD ["streamlit", "run", "app/main.py", \
    "--server.port=8501", \
    "--server.address=0.0.0.0"]