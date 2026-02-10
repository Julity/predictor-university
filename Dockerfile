# Используем конкретную версию Python 3.10
FROM python:3.10.13-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Сначала копируем только requirements.txt для лучшего кэширования
COPY requirements.txt .

# Устанавливаем зависимости в правильном порядке
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    numpy==1.24.3 \
    joblib==1.3.2 && \
    pip install --no-cache-dir -r requirements.txt

# Создаем структуру проекта в контейнере
COPY app/ ./app/
COPY src/ ./src/
COPY config.py ./
COPY models/ ./models/ 2>/dev/null || mkdir -p models

# Проверяем наличие критических файлов
RUN echo "=== Проверка файлов ===" && \
    echo "config.py exists: $(ls -la config.py 2>/dev/null || echo 'NO')" && \
    echo "app/main.py exists: $(ls -la app/main.py 2>/dev/null || echo 'NO')" && \
    echo "src/predictor.py exists: $(ls -la src/predictor.py 2>/dev/null || echo 'NO')" && \
    echo "=== Содержимое проекта ===" && \
    find . -name "*.py" -type f | head -10

# Устанавливаем PYTHONPATH
ENV PYTHONPATH="/app:/app/src"

# Открываем порт
EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD python -c "import sys; sys.exit(0)"

# Запускаем приложение
CMD ["streamlit", "run", "app/main.py", \
    "--server.port=8501", \
    "--server.address=0.0.0.0", \
    "--server.headless=true"]