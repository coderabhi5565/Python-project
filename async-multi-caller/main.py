import asyncio
from apis.llama import call_llama
from apis.mixtral import call_mixtral
from apis.gemma import call_gemma
from retry import call_with_retry
from display import display_results

async def main():
    prompt = input("Enter your prompt: ")
    
    results = await asyncio.gather(
        call_with_retry(call_llama, prompt),
        call_with_retry(call_mixtral, prompt),
        call_with_retry(call_gemma, prompt)
    )
    
    display_results(prompt, results[0], results[1], results[2])

if __name__ == "__main__":
    asyncio.run(main())