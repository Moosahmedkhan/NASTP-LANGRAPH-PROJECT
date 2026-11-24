import os
from langgraph_supervisor import create_supervisor
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from openai import base_url
from core import settings  # noqa: F401  (loads .env)
from modules.ai_agent.tools import TOOLS

def create_chat_model():
    return ChatOpenAI(
        model=os.environ["OPENAI_MODEL"],
        base_url=os.getenv("OPENAI_BASE_URL") OR None,
        temperature=0,

    )
    