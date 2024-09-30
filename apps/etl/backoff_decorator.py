import logging
import random
import time
from functools import wraps


def backoff(
    start_sleep_time=0.1, factor=2, border_sleep_time=10, exceptions=(Exception,)
):
    def func_wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            t = start_sleep_time
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if t < border_sleep_time:
                        t = min(border_sleep_time, t * factor)
                    jitter = random.uniform(0, t)
                    time.sleep(jitter)
                    logging.warning(
                        f"Retrying after exception: {e}. Sleeping for {jitter:.2f} seconds."
                    )

        return inner
    return func_wrapper
