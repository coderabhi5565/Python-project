import asyncio

async def call_with_retry(func,*args,max_retries = 3):
    for i in range(max_retries):
        try:
            return await func(*args)
        except Exception as e:
            wait = 2**i
            print(f"Attempt {i + 1} failed: {e}. Retrying in {wait}s...")
            await asyncio.sleep(wait)
    return "Error: All retries failed"

