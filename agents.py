import os
from agency_swarm import Agent, Agency, set_openai_key
from prompts import (
    planner_description, 
    planner_instructions, 
    researcher_description, 
    researcher_instructions,
    reporter_description,
    reporter_instructions,
    manager_description,
    manager_instructions,
    mission_statement_prompt
    )
from tools import SearchEngine, ScrapeWebsite
from utils import load_config

# loads API keys from config.yaml
load_config(file_path="./config.yaml")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
set_openai_key(OPENAI_API_KEY)

manager = Agent(name="Manager",
            description= manager_description,
            instructions= manager_instructions, # can be a file like ./instructions.md
            # files_folder="./files", # files to be uploaded to OpenAI
            # schemas_folder="./schemas", # OpenAPI schemas to be converted into tools
            # tools=[MyCustomTool], 
            temperature=0, # temperature for the agent
            max_prompt_tokens=25000, # max tokens in conversation history
            )

planner = Agent(name="Planner",
            description= planner_description,
            instructions= planner_instructions,
            temperature=0,
            max_prompt_tokens=25000, 
            )

researcher = Agent(name="Researcher",
            description= researcher_description,
            instructions= researcher_instructions,
            tools=[SearchEngine, ScrapeWebsite], 
            temperature=0,
            max_prompt_tokens=25000,
            )


reporter = Agent(name="Reporter",
            description= reporter_description,
            instructions= reporter_instructions,
            temperature=0,
            max_prompt_tokens=25000,
            )


agency = Agency([
       manager,
       [manager, planner],
       [manager, researcher],
       [manager, reporter],
     ], 
     shared_instructions= mission_statement_prompt,
     temperature=0,
     max_prompt_tokens=25000
)

if __name__ == "__main__":
    agency.run_demo()