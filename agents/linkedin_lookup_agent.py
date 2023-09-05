from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType

from tools_1.tools import get_profile_url


def lookup(name: str, jobtitle: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the company name {name_of_company} and the job title {job_title} I want you to get me a link to the individuals Linkedin profile page. 
                    Your answer should contain only a URL"""  # This is the output indicator

    tool_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to get the Linkedin Page URL when have the Company Name and Job Title",
        )
    ]
    # name -> this is mandatory, each tool should have a unique name, it is the function that will be called when the LLM decides to use the tool
    # description -> not mandatory but the agent decides whether to use the tool or not based on the description

    agent = initialize_agent(
        tools=tool_for_agent,  # List of tools you will be using
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    # Agent type is super important because it determines the reasoning type for the agent
    # Verbose True because it will inform of all the tasks that it is doing (it will show a step by step)

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_company", "job_title"]
    )

    linkedin_profile_url = agent.run(
        prompt_template.format_prompt(name_of_company=name, job_title=jobtitle)
    )
    return linkedin_profile_url
