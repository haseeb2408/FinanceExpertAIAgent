from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()
## websearch Agent
websearch_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information" , 
    model = Groq(id = 'llama-3.3-70b-versatile'),
    tools = [DuckDuckGo()],
    instructions=['Always include the resource'],
    show_tool_calls=True,
    markdown=True
)


## Financial Agent
financial_agent = Agent(
    name = "Financial Agent" , 
    model = Groq(id = 'llama-3.3-70b-versatile'),
    tools =[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True , company_news = True)
        ],
    instructions = ['Use tables to display the Data'],
    show_tool_calls=True , 
    markdown=True
)


multi_agent = Agent(
    model = Groq(id='llama-3.3-70b-versatile'),
    team = [websearch_agent , financial_agent] , 
    instructions = ['Always include the resource' , 'Use tables to display the Data'] , 
    show_tool_calls=True,
    markdown=True
)


multi_agent.print_response("Summarize analyst recomendations and share the lateast news about NVDA" , stream = True)