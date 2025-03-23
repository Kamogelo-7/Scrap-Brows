from langchain_anthropic import ChatAnthropic
from browser_use import Agent, Browser, BrowserConfig, Controller
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
load_dotenv()

import asyncio

class Post(BaseModel):
    caption: str
    url: str

class Posts(BaseModel):
    posts: List[Post]

controller = Controller(output_model=Posts)

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    )
)

# Initialize the model
llm = ChatAnthropic(
    model_name="claude-3-7-sonnet-20250224",
    temperature=0.0,
    timeout=100,
    )

# Create agent with the model
async def main():
   #`initial_actions` a set of actions that the agent will perform when it starts running.
    initial_actions = [
	{'open_tab': {'url': 'https://www.youtube.com'}},
	{'open_tab': {'url': 'https://chatgpt.com/'}},
]

    agent = Agent(
        task="Search for latest news about AI",
        llm=llm,
        browser=browser,
        controller=controller,
        initial_actions=initial_actions,
    )
    print("Running agent...")

    # Debugging: Print before running
    print("Debug: About to start agent.run()")
    result = await agent.run()
    # Debugging: Print after running
    data = result.final_result()
    parsed: Posts = Posts.model_validate_json(data)
    print("Debug: Finished agent.run()")
    print("Agent finished.")
    print(result.final_result())

    await browser.close()


asyncio.run(main())
