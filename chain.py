from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load the environment variables
load_dotenv('.env')

# Define the Google Generative AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,

)

# Define the chat prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Translate {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

# Define the chain
chain = prompt | llm

def translate(input_language, output_language, input):
    """
    Translate the input from the input language to the output language using the Google Generative AI model.
    Args:
        input_language (str): The input language.
        output_language (str): The output language.
        input (str): The input text to translate.
    Returns:
        dict: The translated output text.
    """
    
    response = chain.invoke(
        {
            "input_language": input_language,
            "output_language": output_language,
            "input": input,
        }
    )
    output = response.dict()
    out_dict = {
        "response": output['content'],
        "input_tokens": output['usage_metadata']['input_tokens'],
        "output_tokens": output['usage_metadata']['output_tokens']
        }
    return out_dict
