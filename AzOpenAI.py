import os
from openai import AzureOpenAI

AZURE_OPENAI_ENDPOINT = "https://krsazureopenai2.openai.azure.com/"
AZURE_OPENAI_KEY = "9vaFaSWWMNeEVS7ZBPftkeO8mDLozuOphOiS51RPlYphCXZ5T4h3JQQJ99BFACYeBjFXJ3w3AAABACOGHc3o"
AZURE_OPENAI_DEPLOYMENT_NAME = "KRSAzureOpenAI2"

# Initialize the Azure OpenAI client
try:
    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_KEY,
        api_version="2021-04-30"  # Use an appropriate API version
    )
except TypeError:
    print("One or more of the hardcoded variables are not set.")
    exit()

# The name of your deployment in Azure OpenAI Studio
deployment_name = AZURE_OPENAI_DEPLOYMENT_NAME

# The user's prompt
user_prompt = "Explain the theory of relativity in simple terms."

# Create the chat completion request
try:
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )

    # Print the response from the model
    if response.choices:
        print("AI Response:")
        print(response.choices[0].message.content)
    else:
        print("No response received from the model.")

except Exception as e:
    print(f"An error occurred: {e}")



