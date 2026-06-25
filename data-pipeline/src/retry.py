import time


def retry(func, max_retries=3, delay=2):
    for attempt in range(1, max_retries + 1):
        try:
            return func()

        except Exception as e:
            print(f"Attempt {attempt} Failed: {e}")

            if attempt == max_retries:
                raise

            print(f"Retrying in {delay} seconds...\n")

            time.sleep(delay)