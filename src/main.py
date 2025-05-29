# coding: utf-8
##########################################################################
# Copyright (c) 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0
# as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at
# https://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
##########################################################################
# Reference Link: https://docs.llamaindex.ai/en/stable/examples/llm/oci_genai/
##########################################################################
# Install packages
# pip install -U oci==2.141.1 llama-index==0.12.10 llama-index-llms-oci-genai==0.3.0
##########################################################################
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.agent.workflow import FunctionAgent
from datetime import datetime
from llama_index.core.tools import FunctionTool
from tools import current_date_tool, duckduckgo_tool, oci_cli_tool


import asyncio

# initialize interface
llm = GoogleGenAI(
  model="gemini-2.5-flash-preview-05-20",
  provider="google"
)

# Register all tools
agent = FunctionAgent(tools=duckduckgo_tool + [current_date_tool, oci_cli_tool], llm=llm)

async def chat():
    print("Welcome to the Gemini CLI Chat! Type 'exit' to quit.")
    context = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        context.append({"role": "user", "content": user_input})
        prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in context])
        response = await agent.run(prompt)
        print("Gemini:", getattr(response, "response", str(response)))
        context.append({"role": "assistant", "content": getattr(response, "response", str(response))})

if __name__ == "__main__":
    asyncio.run(chat())
