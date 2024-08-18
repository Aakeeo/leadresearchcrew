from crewai_tools import BaseTool
from dotenv import load_dotenv
import os
import requests


class EmployeesInfoTool(BaseTool):
    name: str = "Employees Info Tool to gather information about employees given a company url"
    description: str = (
        "This tool is used to gather information about employees given a company url."
    )

    def _run(self, domain: str) -> str:
        # Implementation goes here
        load_dotenv()
        ENRICHMENT_API_KEY = os.environ["ENRICHMENT_API_KEY"]
        payload = {'api_key': ENRICHMENT_API_KEY, 'domain':domain}
        resp = requests.get('https://api.enrichmentapi.io/employees', params=payload)
        return resp.text