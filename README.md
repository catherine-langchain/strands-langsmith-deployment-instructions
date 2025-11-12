## Setting up Deployment & Tracing for Strands Agents on LangSmith Deployments

This project demonstrates how to deploy and trace an example strands agent to LangSmith. 

### Clone the repo
```
git clone https://github.com/catherine-langchain/strands-langsmith-deployment-instructions
```

### Create an environment variables file
```
$ cd strands-langsmith-deployment-instructions
cp .env.example .env
```
Fill in fields such as OTel endpoint, headers (project and API key), and AWS credentials. Make sure you disable LangSmith tracing so they are not double traced. 

### Package Installation
Ensure you have a recent version of pip and python installed
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
### Run the agent locally 
Ensure you have a recent version of pip and python installed
```
$ langgraph dev --allow-blocking 
```

### Deploy the agent to LSD 
You can follow the notebook `strands_lsd_walkthrough.ipynb` on building and steps to deploy the agent
