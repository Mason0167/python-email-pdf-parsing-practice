import os
import re
from pypdf import PdfReader

from config import *

def download_attachment(filename, filedata):
    
    # __file__ 是程式檔案路徑
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    save_path = os.path.join(base_dir, PDF_DIR)

    # Ensure the dir exists
    os.makedirs(save_path, exist_ok=True)

    # Complete file path
    file_path = os.path.join(save_path, filename)

    with open(file_path, "wb") as f:
        f.write(filedata)

    print(f"Saved: {file_path}")

# 美股pdf
# def parse_pdf(file_path, password=None):
#     base_dir = os.path.dirname(os.path.abspath(__file__))  
#     file_path = os.path.join(base_dir, file_path)

#     reader = PdfReader(file_path)
#     if reader.is_encrypted:
#         if password is None:
#             raise ValueError(f"{file_path} is encrypted but no password provided")
#         reader.decrypt(password)

#     # Extract Text
#     text = ""
#     for page in reader.pages:
#         page_text = page.extract_text()
#         if page_text:
#             text += page_text + "\n"
       
#     # Choose lines
#     lines = text.splitlines()
#     lines = [line.strip() for line in lines if line.strip()]
    
#     trades = []

#     for line in lines:
#     # Filter by 2 strings
#         if "202" not in line or "-" not in line:
#             continue

#         parts = line.split()
      # 要補買或賣key
#         trade = {
#             "TradeDate": parts[0],
#             "Currency": parts[2],
#             "Ticker": parts[3],
#             "Quantity": parts[5],
#             "ExecutionPrice": parts[6],
#             "Commission": parts[8],
#             "TotalAmount": parts[10]
#         }


# 台新新版pdf
# def parse_pdf(file_path, password=None):
#     base_dir = os.path.dirname(os.path.abspath(__file__))  
#     file_path = os.path.join(base_dir, file_path)

#     reader = PdfReader(file_path)
#     if reader.is_encrypted:
#         if password is None:
#             raise ValueError(f"{file_path} is encrypted but no password provided")
#         reader.decrypt(password)

#     # Extract Text
#     text = ""
#     for page in reader.pages:
#         page_text = page.extract_text()
#         if page_text:
#             text += page_text + "\n"
#             # print(text)
       
#     # Choose lines
#     lines = text.splitlines()
#     lines = [line.strip() for line in lines if line.strip()]

#     trades = [] # list
#     trade = {} # dict
#     full_text = ""
#     buffer = None

    # for line in lines:
    # # Filtering
    # # 偵測空格: r"\s+"
    #     if re.match(r"\d{2}/\d{2}\s+\d{4}", line):
    #         buffer = line
    #         continue
        
    #     if buffer and ("現買" in line or "現賣" in line):
    #         full_text += buffer + " " + line + "\n"
    #         buffer = None

    # for line in full_text.splitlines():
    #     parts = line.split()

    #     # 台股新版pdf
    #     trade = {
    #         "Currency": "TWD",
    #         "TradeDate": parts[0],
    #         "Ticker": parts[1],
    #         "Quantity": parts[2],
    #         "ExecutionPrice": parts[3],
    #         "Commission": parts[4],
    #         "Side": parts[5],
    #         "Company Name": parts[6],
    #         "TotalAmount": parts[8]
    #     }
    #     trades.append(trade)


# 台新舊版zip
def parse_zip(file_path, password=None):
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    file_path = os.path.join(base_dir, file_path)