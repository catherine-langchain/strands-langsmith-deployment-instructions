from strands import Agent
from strands_tools import file_read, file_write, python_repl, shell, journal
from strands.telemetry import StrandsTelemetry
from strands.types.content import Message

from langgraph.func import entrypoint, task
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


@task
def invoke_strands(messages: list[Message]):
    # run the agent with existing messages; can invoke with the final message with messages[-1]
    result = agent(messages) 
    # return the resulting message 
    return [result.message]



@entrypoint()
def workflow(messages: list[Message], previous: list[Message]):
    messages = operator.add(previous or [], messages)
    response = invoke_strands(messages).result()
    return entrypoint.final(value=response, save=operator.add(messages, response))


# user_message: Message = [{
#     "role": "user",
#     "content": [
#         {"text": "Do a short review of /Users/qiaocatherine/Documents/Fortune1000_SFDC_First20.csv. Focus on key functionality."}
#     ]
# }]

# for chunk in workflow.stream(user_message):
#     print(chunk)