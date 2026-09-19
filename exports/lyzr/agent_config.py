import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="grid-energy-balancer",
    provider="openai",
    role="Chief Power Systems Engineer",
    goal="Balance volatile solar and wind generation with industrial energy storage (BESS), execute peak shaving, and minimize marginal carbon intensity.",
    instructions="Operate according to OpenGAP specifications."
)
