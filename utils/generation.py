from google.genai.types import GenerateContentConfig

generation_config = GenerateContentConfig(

    temperature=0.3,

    top_p=0.9,

    max_output_tokens=1024
)
