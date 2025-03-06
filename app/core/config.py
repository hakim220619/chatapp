import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/chatbot")
SECRET_KEY = os.getenv("SECRET_KEY", "jasjdhgasdhe625374rt38y93rywegfywer374rejwvdweg")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
