# crew.py (Simplified code to define the workflow)
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from tools import setup_search_tool # Assuming you put the search tool in tools.py

# 1. Setup the Local LLM (The Zero-Cost Brain)
ollama_llm = Ollama(model="mistral", base_url="http://localhost:11434")
search_tool = setup_search_tool()

# 2. Define the AGENTS
# Agent 1: The Recon Agent (Collector)
recon_agent = Agent(
    role='Public Digital Footprint Collector',
    goal='Search the web and gather all public links, emails, and usernames associated with the input name.',
    backstory="A specialized OSINT investigator focused on public data. You are a thorough collector.",
    tools=[search_tool],
    llm=ollama_llm,
    allow_delegation=False,
    verbose=True
)

# Agent 2: The Clustering & Risk Scoring Agent (The UNIQUE AI Twist)
risk_agent = Agent(
    role='Digital Risk Analyst',
    goal='Analyze the collected data, cluster it into groups (e.g., Professional, Personal, Gaming), and assign a final risk score (1-10) with remediation advice.',
    backstory="An expert in cybersecurity, translating raw data into actionable risk insights and clear remediation steps.",
    llm=ollama_llm,
    allow_delegation=False,
    verbose=True
)

# 3. Define the TASKS
def run_footprint_analysis(target_name):
    # Task 1: Find all public mentions and links
    collection_task = Task(
        description=f"Using the Web Search Tool, find all public social media profiles, email addresses, and public links for the name: {target_name}. Compile a simple list of raw findings.",
        expected_output="A clean, numbered list of all raw links, usernames, and email addresses found.",
        agent=recon_agent
    )

    # Task 2: The Unique Twist (Clustering and Scoring)
    analysis_task = Task(
        description="TAKE THE RAW FINDINGS from the Collection Agent. 1. Cluster the data into logical groups (e.g., 'Professional,' 'Personal,' 'Hobby'). 2. Assign a risk score (1-10, 10 is highest risk) based on the exposure. 3. Write 3 actionable steps to reduce the risk. Format the final output clearly.",
        expected_output="A final report with three sections: 1) Overall Risk Score and Justification, 2) Clustered Data, 3) 3 Actionable Remediation Steps.",
        agent=risk_agent
    )

    # 4. Create the Crew and Run
    footprint_crew = Crew(
        agents=[recon_agent, risk_agent],
        tasks=[collection_task, analysis_task],
        process=Process.sequential, # Run Task 1, then Task 2
        verbose=2 # Show step-by-step progress
    )

    result = footprint_crew.kickoff()
    return result