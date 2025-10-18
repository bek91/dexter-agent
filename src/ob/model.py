import os
from datetime import datetime, timezone
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Type, List, Optional
from langchain_core.tools import BaseTool
from langchain_core.messages import AIMessage

from ob.prompts import DEFAULT_SYSTEM_PROMPT
from ob.schemas import Answer as AnswerSchema

# Defaults for guardrails if DEFAULT_SYSTEM_PROMPT is used
DEFAULT_MAX_STEPS = int(os.getenv("OB_MAX_STEPS", "20"))
DEFAULT_MAX_STEPS_PER_TASK = int(os.getenv("OB_MAX_STEPS_PER_TASK", "5"))

# Initialize OpenAI clients
# Default model for planning/action/validation, answer model for final answer generation
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = os.getenv("OB_LLM_MODEL", "gpt-4o")
ANSWER_MODEL = os.getenv("OB_ANSWER_LLM_MODEL", "gpt-5-mini")

llm_default = ChatOpenAI(model=DEFAULT_MODEL, temperature=0, api_key=OPENAI_API_KEY)
llm_answer = ChatOpenAI(model=ANSWER_MODEL, temperature=0.4, api_key=OPENAI_API_KEY)

def call_llm(
    prompt: str,
    system_prompt: Optional[str] = None,
    output_schema: Optional[Type[BaseModel]] = None,
    tools: Optional[List[BaseTool]] = None,
) -> AIMessage:
  # Choose the system prompt (phase-specific or default), inject current UTC time,
  # and fill placeholders if using the default prompt.
  now_iso = datetime.now(timezone.utc).isoformat()
  if system_prompt:
      base_prompt = system_prompt
  else:
      try:
          base_prompt = DEFAULT_SYSTEM_PROMPT.format(
              max_steps=DEFAULT_MAX_STEPS,
              max_steps_per_task=DEFAULT_MAX_STEPS_PER_TASK,
          )
      except Exception:
          base_prompt = DEFAULT_SYSTEM_PROMPT
  final_system_prompt = f"{base_prompt}\n\nCurrent datetime (UTC): {now_iso}"
  
  prompt_template = ChatPromptTemplate.from_messages([
      ("system", final_system_prompt),
      ("user", "{prompt}")
  ])

  # Select model: use answer model only when producing the final structured Answer
  base_llm = llm_answer if (output_schema is AnswerSchema) else llm_default

  runnable = base_llm
  if output_schema:
      runnable = base_llm.with_structured_output(output_schema)
  elif tools:
      runnable = base_llm.bind_tools(tools)
  
  chain = prompt_template | runnable
  return chain.invoke({"prompt": prompt})
