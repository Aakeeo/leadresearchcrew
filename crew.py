from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from tools.EmployeesInfoTool import EmployeesInfoTool
from tools.FindPersonalInfo import FindPersonalInfo

# Uncomment the following line to use an example of a custom tool
# from sales_bd_project.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class SalesBdProjectCrew():
	"""SalesBdProject crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	SearchTool = SerperDevTool()
	EmployeesInfoTool = EmployeesInfoTool()
	FindPersonalInfo = FindPersonalInfo()

	@agent
	def company_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['company_researcher'],
			tools=[self.SearchTool], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def employee_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['employee_researcher'],
			tools=[self.EmployeesInfoTool,self.FindPersonalInfo], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	
	@agent
	def research_consolidator(self) -> Agent:
		return Agent(
			config=self.agents_config['research_consolidator'],
			tools=[], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	
	@task
	def company_bio_task(self) -> Task:
		return Task(
			config=self.tasks_config['company_bio_task'],
			tools=[self.SearchTool],
		)
	
	@task
	def employee_info_task(self) -> Task:
		return Task(
			config=self.tasks_config['employee_info_task'],
			tools=[self.EmployeesInfoTool],
		)
	
	@task
	def consolidate_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['consolidate_research_task'],
			tools=[],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the SalesBdProject crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)