from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.gemini import Gemini
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

cart = []
wishlist = []


llm = Ollama(
        model="mistral-nemo:latest",
        # model = "gpt-oss:20b",
        temperature=0.3,
        context_window=8000,
        # thinking=False,
)

Settings.llm = llm  # same instance

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
documents = SimpleDirectoryReader("data").load_data()
print(f"✅ Loaded {len(documents)} documents from data/")
if len(documents) > 0:
    print("Sample document:\n", documents[0].text[:500])
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Make the search function synchronous
def search_furniture_products(query: str) -> str:
    print("Using search_furniture_products function")
    """
    Search for furniture products in the store inventory.
    
    Use this when the user asks about:
    - Product details (materials, dimensions, colors, features)
    - Prices and availability
    - Specific furniture items (sofas, tables, chairs, beds, etc.)
    - Comparisons between products
    - Product recommendations
    - Customer support
    - Warranty
    - Delivery
    
    Args:
        query: Natural language question about furniture products
        
    Returns:
        Detailed information about the requested furniture items
        
    Examples:
    - "What dining tables do you have under $500?"
    - "Tell me about leather recliners"
    - "What's the material of the Oak Dining Table?"
    """

    # Use synchronous query instead
    response = query_engine.query(query)
    print("="*10,"Response from LLM : ","="*10)
    print(response)
    print("="*10,"Agent response : ","="*10)
    return str(response)

def addToCart(item)->str:
    """Useful for adding an item to the cart"""
    cart.append(item)
    return "Item added to the cart"

def addToWishlist(item)->str:
    """Useful for adding an item to the wishlist"""
    wishlist.append(item)
    return "Item added to the wishlist"

agent = FunctionAgent(
    tools=[addToCart, search_furniture_products, addToWishlist],
    llm=llm,
    system_prompt="""
You are a helpful and strict furniture store assistant.

Your main capabilities:
1. **Search products** — via `search_furniture_products`
2. **Add to cart** — via `addToCart`
3. **Add to wishlist** — via `addToWishlist`

RULES (follow these exactly):

- If the user asks **anything** about available items, furniture categories, prices, materials, colors, availability, or product details, 
  **you MUST call `search_furniture_products` immediately** before responding.
  
- If the user mentions adding an item to their cart, 
  **you MUST call `addToCart`** with the exact product name returned by `search_furniture_products`.

- If the user mentions saving an item for later, 
  **you MUST call `addToWishlist`** with the exact product name returned by `search_furniture_products`.

- Never answer about products from memory. Always use the function to fetch the correct information.
- After getting the data, summarize it nicely for the user.
- If the product name is unclear, ask the user for clarification.

### Example Flow:

**User:** "What sofas do you have?"
→ Call `search_furniture_products("sofas available")`
→ Show all sofas.

**User:** "I’ll take the Modern Leather Sofa"
→ Call `addToCart("Modern Leather Sofa")`
→ Confirm the addition.

**User:** "Save the Wooden Dining Table for later"
→ Call `addToWishlist("Wooden Dining Table")`
→ Confirm the addition.

When you use search_furniture_products, always show the full retrieved text directly to the user. Do not summarize or hide results.
If you do not call any function when required, you are breaking your own rules.
"""
)
