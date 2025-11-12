from strands import Agent
from strands_tools import file_read, file_write, python_repl, shell, journal
from strands.telemetry import StrandsTelemetry
from strands.types.content import Message

from langgraph.graph import StateGraph, START
from typing_extensions import TypedDict, Annotated
import operator
from dotenv import load_dotenv






load_dotenv()


strands_telemetry = StrandsTelemetry()
strands_telemetry.setup_otlp_exporter()
strands_telemetry.setup_meter()


agent = Agent(
        tools=[file_read, file_write, python_repl, shell, journal],
        system_prompt="You are an Expert Software Developer specializing in web frameworks. Your task is to analyze project structures and identify mappings.",
        model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    )




class State(TypedDict):
    # keep track of all messages in the conversation
    messages: Annotated[list[Message], operator.add]  

# Define the agent graph
def agent_graph(state: State):
    # run the agent with existing messages 
    result = agent(state["messages"])
    # return the new message in the state return 
    return {"messages": [result.message]}


# Build and Compile the graph
builder = StateGraph(State)
builder.add_node("strands", agent_graph)
builder.add_edge(START, "strands")
graph = builder.compile()

