# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key
#from google.colab import userdata

GOOGLE_API_KEY = "AIzaSyAfIOlzJwUyxHK0CwOfuEl2NlCvTIqbGRI"
#GOOGLE_API_KEY = "AIzaSyBtWs8Jab01LbWAgGZeMP9zyCIVxXcqu3k"
#GOOGLE_API_KEY = "AIzaSyAtjkSltUXhtYbEvycxcD8Qr6Q7t89Vpoc"

# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


#model = genai.GenerativeModel('gemini-1.5-pro')
model = genai.GenerativeModel('gemini-1.5-flash-8b-exp-0827')
model = genai.GenerativeModel('gemini-1.5-flash-exp-0827')
#model1 = genai.GenerativeModel('gemini-1.5-flash')




#prompt = """
#You are the super intelligence to extract transaction from image\n\n
#  {image}\n\n
#priority - give only all transactions, which always starting from Date Descriptions Amount header otherwise not\n
#headers of list are - Date,Descriptions,Amount.
#Don't give cheque forms transactions and header of text.\n
#if you found empty image then return empty list\n
#give only list of dictionaries don't give code\n
#Don't take total amount and any of header have null value.\n
#Don't give ``` start and end of list.
#"""
#

#prompt1="""
#You are a highly advanced AI specializing in transaction extraction from images.
#
#{image}
#
#your task is to extract only the valid transactions that starting from the headers: "Date", "Descriptions", and "Amount" otherwise, Don't give." 
#Instructions:
#Focus exclusively on transactions that have a clear header with the fields: Date, Descriptions, and Amount.
#If the image contains no transactions, return an empty list.
#Ensure each transaction is represented as a dictionary.
#Exclude transactions where any of the header fields (Date, Descriptions, or Amount) have missing values.
#Don't give header texts transactions, or total amounts.
#skip cheque(check) forms image for extracting transactions.
#Return only a list of dictionaries, without including any code blocks (e.g., avoid wrapping the list in ```).
#"""
#
prompt2="""
You are a highly advanced AI specializing in transaction extraction from images.

{image}

Your task is to extract only valid transactions that start with the headers: "Date", "Descriptions", and "Amount". If no valid transactions are found, return an empty list.

Instructions:
Focus exclusively on transactions that follow the headers: Date, Descriptions, and Amount.
**Do not extract transactions related to cheques/checks** (ignore cheque/check form images entirely).
Skip transactions where any of the fields (Date, Descriptions, or Amount) have missing or null values.
Ignore header texts, total amounts, and any non-transactional data.
If the image contains no valid transactions, return an empty list.
Return only a list of dictionaries for valid transactions not code, and avoid wrapping ``` the output list.

Be precise and exclude any cheque/checks-related content.
"""


prompt="""
You are an advanced AI that extracts transactions from Bank Statement image.

Input_image:
{image}

Your task is to extract all transactions from above image, transactions always starting from DATE, DESCRIPTION, AMOUNT header very strictly. if you find headers  CREDIT, DEBIT, and BALANCE then include them othrwise exclude it, then ignore them .

Instructions:
at least these 3 columns should be present in image other wise ignore/give empty list.
Find and focus only on all transactions that come after above headers, otherwise ignore them.
include continued transactions.
Do not include any cheque/check-related transactions.
Do not include header text, total amounts, or unrelated data.
If there are no transactions in image, return an empty list.
Avoid returning null values for any field, try to find a valid value for each.
Output only a list of dictionaries, without any code formatting.
"""

import time
import random

def extr_trans(img):
    max_retries = 5
    retry_delay = 5  # initial retry delay in seconds
    max_retry_delay = 30  # maximum retry delay in seconds

    for attempt in range(max_retries):
        try:
            response = model.generate_content(
                [prompt, img],
                generation_config=genai.types.GenerationConfig(temperature=0)
            )
            return response.text
        except Exception as e:
            if e.status_code == 429:  # Resource Exhausted
                print(f"Received 429 error. Retrying (attempt {attempt+1}/{max_retries})...")
                retry_delay *= 2  # exponential backoff
                retry_delay = min(retry_delay, max_retry_delay)
                time.sleep(retry_delay + random.uniform(0, 1))  # add some randomness to avoid thundering herd
            else:
                raise  # re-raise other exceptions

    print("Maximum retries exceeded. Giving up.")
    return None  # or raise an exception, depending on your requirements

    
    
 
#    
#    
