from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api


import os
from phi.playground import Playground , serve_playground_app


phi.api = os.getenv("PHI_API_KEY")

## websearch Agent
websearch_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information" , 
    model = Groq(id = 'llama3-groq-70b-8192-tool-use-preview'),
    tools = [DuckDuckGo()],
    instructions='Always include the resource',
    show_tool_calls=True,
    markdown=True
)


## Financial Agent
financial_agent = Agent(
    name = "Financial Agent" , 
    model = Groq(id = 'llama3-groq-70b-8192-tool-use-preview'),
    tools =[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True , company_news = True)
        ],
    instructions = ['Use tables to display the Data'],
    show_tool_calls=True , 
    markdown=True
)


app = Playground(agents = [financial_agent, websearch_agent]).get_app()


if __name__ == '__main__':
    serve_playground_app("playground:app" , reload = True)