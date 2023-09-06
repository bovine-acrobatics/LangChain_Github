from dotenv import load_dotenv
import os

# You need this when using a conda environment so that the env variables are loaded
load_dotenv()

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

# This is the inputs for the prompt
import sys

print(sys.path)
sys.path.append("/Users/affanfawzy/Desktop/LangChain_Training/ice_breaker")

if __name__ == "__main__":
    print("hello LangChain!")

    comp_name = "Legal & General"
    job_ttl = "Chief Actuary"

    linkedin_profile_url = linkedin_lookup_agent(name=comp_name, jobtitle=job_ttl)

    print(linkedin_profile_url)
