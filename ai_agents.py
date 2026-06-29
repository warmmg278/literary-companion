from dotenv import load_dotenv
from agents import Agent, Runner
import asyncio

from prompts import (
    IMAGE_AGENT_PROMPT,
    FEEDBACK_AGENT_PROMPT,
)

load_dotenv()



# -----------------------------
# Agent 1 : 시적 이미지 추출
# -----------------------------

image_agent = Agent(
    name="Image Agent",
    instructions=IMAGE_AGENT_PROMPT
)

# -----------------------------
# Agent 2 : 피드백
# -----------------------------

feedback_agent = Agent(
    name="Feedback Agent",
    instructions=FEEDBACK_AGENT_PROMPT
)


async def run_image_agent(emotion, scene):

    prompt = f"""
감정

{emotion}

장면

{scene}
"""

    result = await Runner.run(
        image_agent,
        prompt
    )

    return result.final_output


async def run_feedback_agent(writing):

    result = await Runner.run(
        feedback_agent,
        writing
    )

    return result.final_output