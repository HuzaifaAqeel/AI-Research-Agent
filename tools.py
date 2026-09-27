from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.tools import Tool
from datetime import datetime
import functools
import time

import wikipedia

# Wikipedia's API policy requires a descriptive User-Agent; without it the
# requests are rejected (HTTP 403) by egress filters/proxies.
wikipedia.set_user_agent("AI-Research-Agent/1.0")


def _with_retry(func, attempts=3, delay=2.0):
    """Retry a tool call a few times: transient network/proxy hiccups
    (connection resets) are common when hitting public APIs."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        last_error = None
        for _ in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:  # noqa: BLE001
                last_error = e
                time.sleep(delay)
        raise last_error

    return wrapper


search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=_with_retry(search.run),
    description="search the web for information",
    handle_tool_error=True,
)

class RetryingWikipediaAPIWrapper(WikipediaAPIWrapper):
    """Same wrapper, but retries transient network/proxy failures."""

    def run(self, query: str) -> str:  # type: ignore[override]
        return _with_retry(super().run)(query)


api_wrapper = RetryingWikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=2000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
wiki_tool.handle_tool_error = True