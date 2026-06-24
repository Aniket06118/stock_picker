from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from pydantic import BaseModel , Field
from typing import List


class Trending_Company(BaseModel):
    """A company that is in the news and attracting attention"""
    name: str = Field(description="company name")
    ticker: str = Field(description="stock ticker symbol")
    reason: str = Field(description="reason this company is trending in the news")

class Trending_company_list(BaseModel):
    """list of multiple trending companies that are in the news"""
    companies: List[Trending_Company] = Field(description="list of companies trending in the news")

class TrendingCompanyResearch(BaseModel):
    """Detailed research on a company"""

    name: str = Field(description="Company name")
    market_position: str = Field(description="Current market position and competitive analysis")
    future_outlook: str = Field(description="Future outlook and growth prospects")
    investment_potential: str = Field(description="Investment potential and suitability for investment")

class TrendingCompanyResearchList(BaseModel):
    """A list of detailed research on all the companies"""

    research_list: List[TrendingCompanyResearch] = Field( description="Comprehensive research on all trending companies")





@CrewBase
class StockPicker():
    """StockPicker crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_company_finder'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )
    
    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_picker'], # type: ignore[index]
            verbose=True,
        )

    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_companies'],
            output_pydantic = Trending_company_list # type: ignore[index]
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'], # type: ignore[index]
            output_pydantic= TrendingCompanyResearchList
        )
    
    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_company'], # type: ignore[index]
        )
    
    

    @crew
    def crew(self) -> Crew:
        """Creates the StockPicker crew"""

        manager=Agent(config=self.agents_config['manager'],
                      allow_delegation=True
                      )
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager
        )
