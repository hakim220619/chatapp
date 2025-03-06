FROM python:3.9-slim

# Install sistem dependensi untuk PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev

# Direktori kerja
WORKDIR /app

# Salin file requirements.txt
COPY requirements.txt .

# Instal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin aplikasi ke dalam container
COPY . .

# Expose port 8000
EXPOSE 8000

# Jalankan aplikasi
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
