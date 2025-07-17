from pathlib import Path
from dotenv import load_dotenv
import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
import openai

# Load environment variables from .env in project root
env_path = Path(__file__).resolve().parent.parent / ".env"
print(f"Loading .env from: {env_path}")
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENROUTER_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX_NAME = "college-chatbot"

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY is missing from .env!")
if not PINECONE_API_KEY:
    raise ValueError("❌ PINECONE_API_KEY is missing from .env!")
if not PINECONE_ENV:
    raise ValueError("❌ PINECONE_ENVIRONMENT is missing from .env!")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# Check if index exists; if not, create it
if PINECONE_INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(PINECONE_INDEX_NAME, dimension=1536)

index = pinecone.Index(PINECONE_INDEX_NAME)
embedding_model = OpenAIEmbeddings()

def get_chat_response(query: str) -> str:
    # 1. Embed query
    query_embedding = embedding_model.embed_query(query)

    # 2. Query Pinecone index for top 3 relevant chunks
    results = index.query(query_embedding, top_k=3, include_metadata=True)

    # 3. Build context from retrieved metadata texts
    context = "\n".join([match['metadata']['text'] for match in results['matches']])

    # 4. Prepare prompt for OpenRouter/OpenAI
    prompt = f"Context:\n{context}\n\nUser question: {query}\nAnswer:"

    # 5. Call OpenAI completion endpoint
    response = openai.Completion.create(
        engine="openai-chat",  # Replace with your engine if different
        prompt=prompt,
        max_tokens=150,
        temperature=0.2,
        n=1,
        stop=None,
    )

    answer = response.choices[0].text.strip()
    return answer
