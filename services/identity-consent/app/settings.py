import os

POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://akeno:akeno@localhost:5433/akeno")
