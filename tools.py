\# tools.py



\# Step 1: Import the necessary tool class

from langchain\_community.tools import DuckDuckGoSearchRun



\# Step 2: Define a function to initialize and return the tool

def setup\_search\_tool():

&nbsp;   """

&nbsp;   Initializes and returns a web search tool using DuckDuckGo.

&nbsp;   This is free and doesn't require an API key.

&nbsp;   """

&nbsp;   # The 'name' is optional but good practice.

&nbsp;   return DuckDuckGoSearchRun(name="Web Search Tool") 



\# Remember to run: pip install duckduckgo-search in your terminal!

