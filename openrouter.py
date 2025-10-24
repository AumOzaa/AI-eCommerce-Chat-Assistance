from llama_index.llms.openrouter import OpenRouter

llm = OpenRouter(
    api_key="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",
    max_tokens=256,
    context_window=4096,
    model="deepcogito/cogito-v2-preview-llama-405b",
)

response = llm.complete("Hello World!")
print(str(response))
