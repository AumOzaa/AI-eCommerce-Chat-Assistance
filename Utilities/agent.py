from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.gemini import Gemini
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

cart = []
wishlist = []

# Make the search function synchronous
def search_furniture_products(query: str) -> str: #todo : Pass the query engine here.
    """
    Search for furniture products in the store inventory.
    
    Use this when the user asks about:
    - Product details (materials, dimensions, colors, features)
    - Prices and availability
    - Specific furniture items (sofas, tables, chairs, beds, etc.)
    - Comparisons between products
    - Product recommendations
    
    Args:
        query: Natural language question about furniture products
        
    Returns:
        Detailed information about the requested furniture items
        
    Examples:
    - "What sofas do you have under $500?"
    - "Tell me about leather recliners"
    - "What's the material of the Oak Dining Table?"
    """

    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    # Use synchronous query instead
    response = query_engine.query(query)
    return str(response)

def addToCart(item)->str:
    """Useful for adding an item to the cart"""
    cart.append(item)
    return "Item added to the cart"

def addToWishlist(item)->str:
    """Useful for adding an item to the wishlist"""
    wishlist.append(item)
    return "Item added to the wishlist"

# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    tools=[addToCart,search_furniture_products,addToWishlist],
    llm=Gemini(
    model="gemini-2.5-flash",
    api_key="AIzaSyDiLGcptDvMcSYNzx_",  # todo : make the API in env folder.
),
    system_prompt="""You are a helpful furniture store assistant. 

Your capabilities:
1. **Search products**: Use search_furniture_products to answer questions about furniture items, prices, materials, availability, or features
2. **Add to cart**: Use add_to_cart when customers want to purchase items
3. **Add to wishlist**: Use add_to_wishlist when customers want to save items for later

Important guidelines:
- ALWAYS use search_furniture_products FIRST when users ask about products, prices, or details
- Only add items to cart/wishlist AFTER the customer has seen product information
- Use the exact product names returned from search results
- Be helpful and ask clarifying questions if needed

Example flow:
User: "What sofas do you have?"
→ Use search_furniture_products("sofas available")
→ Present results to user
User: "I'll take the Modern Leather Sofa"
→ Use add_to_cart("Modern Leather Sofa")
""",
)