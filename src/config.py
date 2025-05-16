# src/config.py

# TCFD/CDP-aligned disclosure questions to extract
CLIMATE_DISCLOSURE_QUESTIONS = [
    "What is the company's Scope 1 GHG emissions?",
    "What is the company's Scope 2 GHG emissions?",
    "What is the company's Scope 3 GHG emissions?",
    "What net-zero or climate targets has the company disclosed?",
    "What does the company report about climate-related risks and opportunities?",
    "Does the company use any climate scenario analysis (e.g., 1.5°C, 2°C)?",
    "How does the company describe its board-level ESG or climate governance?",
    "Does the company disclose its renewable energy usage or transition strategy?",
    "Does the company disclose use of internal carbon pricing?"
]

# Optional: Keywords you can use to enhance filtering or prompt context
ESG_KEYWORDS = [
    "Scope 1 emissions", "Scope 2 emissions", "Scope 3 emissions",
    "net-zero", "climate target", "TCFD", "carbon price", "renewable energy",
    "climate risk", "climate scenario analysis", "climate governance",
    "CDP", "energy mix", "carbon neutrality"
] 

# Framework tags for potential use in prompting or labeling
FRAMEWORK_TAGS = ["TCFD", "CDP", "CSRD", "SASB"]
