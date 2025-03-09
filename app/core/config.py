import os
from dotenv import load_dotenv

# Muat variabel lingkungan dari file .env
load_dotenv()

# Ambil URL database dan variabel lain dari environment variable
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")  # Set default value jika tidak ada
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 300))  # Convert to integer, default 30

