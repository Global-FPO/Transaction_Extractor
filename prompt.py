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
#model1 = genai.GenerativeModel('gemini-1.5-flash')




prompt = """
You are the super intelligence to extract transaction from image\n\n
  {image}\n\n
priority - give only all transactions, which always starting from Date Descriptions Amount header otherwise not\n
headers of list are - Date,Descriptions,Amount.
Don't give cheque forms transactions and header of text.\n
if you found empty image then return empty list\n
give only list of dictionaries don't give code\n
Don't take total amount and any of header have null value.\n
Don't give ``` start and end of list.
"""


prompt1="""
You are a highly advanced AI specializing in transaction extraction from images.

{image}

your task is to extract only the valid transactions that starting from the headers: "Date", "Descriptions", and "Amount" otherwise, Don't give." 
Instructions:
Focus exclusively on transactions that have a clear header with the fields: Date, Descriptions, and Amount.
If the image contains no transactions, return an empty list.
Ensure each transaction is represented as a dictionary.
Exclude transactions where any of the header fields (Date, Descriptions, or Amount) have missing values.
Don't give header texts transactions, or total amounts.
skip cheque(check) forms image for extracting transactions.
Return only a list of dictionaries, without including any code blocks (e.g., avoid wrapping the list in ```).
"""

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


def extr_trans(img):
 
  #organ = PIL.Image.open('/content/drive/MyDrive/ocr/Screenshot 2024-09-06 132702.png')
  
    # Generate the content in streaming mode
  response = model.generate_content(
      [prompt2, img],
      generation_config=genai.types.GenerationConfig(temperature=0)
      #stream=True
  )
  
  #print(response.text)
  return response.text

    
    
 
#    
#    
