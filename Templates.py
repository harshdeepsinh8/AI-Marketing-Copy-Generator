from langchain_core.prompts import PromptTemplate

marketing_prompt = PromptTemplate.from_template(
    """
    Generate a marketing ad copy for the following details:
    Brand: {brand}
    Product/Service: {description}
    Target Audience: {audience}
    Tone: {tone}

    Provide:
    - A catchy headline
    - A short marketing description (2-3 sentences)
    - Three relevant hashtags
    - A call-to-action (CTA)
    """
)
