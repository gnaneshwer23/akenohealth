import os


POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://akeno:akeno@localhost:5432/akeno")
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "akeno1234")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC_INGESTION = os.getenv("KAFKA_TOPIC_INGESTION", "akeno.ingestion.events")
KAFKA_TOPIC_INGESTION_DLQ = os.getenv("KAFKA_TOPIC_INGESTION_DLQ", "akeno.ingestion.events.dlq")
KAFKA_PUBLISH_RETRIES = int(os.getenv("KAFKA_PUBLISH_RETRIES", "3"))
