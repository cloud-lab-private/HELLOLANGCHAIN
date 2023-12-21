"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import os
import unittest

import langchain_core.messages.ai
from langchain.chat_models import AzureChatOpenAI
from main.lab import lab


class TestLLMResponse(unittest.TestCase):
    """
    This test will verify that the connection to an external LLM is made. If it does not
    work, this may be because the API key is invalid, or the service may be down.
    If that is the case, this lab may not be completable.
    """

    def test_llm_sanity_check(self):
        deployment = os.environ['DEPLOYMENT_NAME']
        llm = AzureChatOpenAI(deployment_name=deployment, model_name="gpt-35-turbo")

    """
    The variable returned from the lab function should be an langchain AI response. If this test
    fails, then the AI message request either failed, or you have not properly configured the lab function
    to return the result of the LLM chat.
    """

    def test_lab_ai_response(self):
        result = lab()
        self.assertIsInstance(result, langchain_core.messages.ai.AIMessage)

    """
    The message response returned from the lab method should contain "hello llm"
    (not case or punctuation sensitive.)
    """

    def test_hello_llm_response(self):
        result = lab()
        content = result.content.lower()
        self.assertIn("hello", content)  # Verifies if "hello" is present in the result
        self.assertIn("llm", content)  # Verifies if "world" is present in the result


if __name__ == '__main__':
    unittest.main()
