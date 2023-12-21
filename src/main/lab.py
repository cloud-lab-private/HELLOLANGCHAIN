import os
from langchain.chat_models import AzureChatOpenAI

"""
All requests to the LLM require some form of a key.
Other sensitive data has also been hidden through environment variables.
"""
api_key = os.environ['OPENAI_API_KEY']
base_url = os.environ['OPENAI_API_BASE']
deployment = os.environ['DEPLOYMENT_NAME']
version = os.environ['OPENAI_API_VERSION']

"""
This function interacts with an LLM and will prompt it for some
generic response. The function will return the response JSON. Langchain acts as an
abstraction layer around the process of interacting with an LLM, so that we may avoid
making detailed HTTP requests, and can remain more agnostic to the respective LLM's API.

The most basic way to interact with the LLM is to use the llm.invoke method. The first
argument passed to the invoke is the prompt, for instance, calling llm.invoke("tell me a joke")
will return an AIMessage response containing the LLM's response. The AIMessage object
will contain the message text of the AI's response.

TODO: Within this function, retrieve an AI response from the provided llm object (AzureChatOpenAI)
that contains a 'hello llm' response by instructing the LLM to say 'hello llm'. The test cases will verify that the 
function produces the expected JSON format, and that it contains a 'hello llm' message.

You can read more about the LLM object's capabilities here, which includes producing
LLM generations across arrays of data with 'apply' and interpolating data into a String
template:
https://python.langchain.com/docs/modules/chains/foundational/llm_chain
"""


def lab():
    llm = AzureChatOpenAI(deployment_name=deployment, model_name="gpt-35-turbo")
    return "todo"
