import streamlit as st
#from pdf2image import convert_from_path
import os
import tempfile
from prompt import extr_trans
import pandas as pd
import time
import fitz
from PIL import Image



st.title("Upload Bank Statements")
# File uploader widget
uploaded_file = st.file_uploader("Choose a file from directory",type=["pdf"])


if uploaded_file is not None:

    st.write('Your Document Uploaded Succesfully')


    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    with st.spinner('Extracting Transactions....'):
        

        
            # Now use convert_from_path with the temp file path                                             
            
        all_text=[]
        pdf_document = fitz.open(temp_file_path)
            
            # Loop through each page
        for page_num in range(len(pdf_document)):
                # Get the page
            page = pdf_document.load_page(page_num)
            
                # Render the page to an image (pixmap)
            pix = page.get_pixmap()
            
                # Convert the pixmap to a PIL Image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
                # Save the image to a file
                # img_path = f'page_{page_num + 1}.png'
                #img.save(img_path)
            
                # Display the image
                #img.show()
            all_text.append(extr_trans(img))
            
            # Close the PDF file
        pdf_document.close()

                
            #    time.sleep(30)
            #all_text=[]
            #for p,img in images:
            #    if p==5:
            #        print(p)
            #        width, height = img.size
#
            #        # Define the split points (e.g., to split into three vertical parts)
            #        split1 = width // 2
            #        split2 = 2 * (width // 2)
            #    
            #        # Crop the three parts
            #        part1 = img.crop((0, 0, split1, height))
            #        #part1.save("part1.jpg")
            #    
            #        part2 = img.crop((split1, 0, split2, height))
            #        #part2.save("part2.jpg")
            #    
            #        part3 = img.crop((split2, 0, width, height))
            #        part3.save("part3.jpg")
            #    
            #        # Define a list of parts to process
            #        parts = [part1, part2, part3]
            #    
            ## Pr    ocess each half
            #        for i, half in enumerate(parts):
            #            all_text.append(extr_trans(half))
            #            time.sleep(36)
            #      
                    
     
                
            
     
        
            
    
        import ast
        ll=[]
        for page,i in enumerate(all_text):
            
            print(f'--page {page+1}')
            
             # i=i.replace('```','"""').strip()
            try:
                start=i.find('[')
                last=i.find(']')
                text=i[start:last+1]
            
                j= ast.literal_eval(text)
            except Exception as e:
            
                   #print(i)
                print(e)
                   #print()
                   #print(type(j))
                   #print(i)
                continue
            for ii in j:
                ll.append(ii)
                   
                   
                   
               
        data_lowercase = [{k.title(): v for k, v in item.items()} for item in ll]
                
                # Pretty-print the list of dictionaries
            #pprint.pprint(data_lowercase)   
                            
        df=pd.DataFrame(data_lowercase)
        st.subheader('Your Transactions :')
        st.write(df)           
               
           
    
