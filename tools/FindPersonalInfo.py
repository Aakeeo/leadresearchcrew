from crewai_tools import BaseTool
from dotenv import load_dotenv
import os
import requests

class FindPersonalInfo(BaseTool):
    name: str = "Find Personal Info Tool to get the Personal Information of a person given a linkedin url"
    description: str = (
        "This tool is used to get the Personal Information of a person given a linkedin url."
    )

    def _run(self, linkedin_url: str) -> str:
        # Implementation goes here
        load_dotenv()
        ENRICHMENT_API_KEY = os.environ["ENRICHMENT_API_KEY"]
        payload = {'api_key': ENRICHMENT_API_KEY, 'linkedin_id':linkedin_url}
        resp = requests.get('https://api.enrichmentapi.io/person', params=payload)
        return resp.text