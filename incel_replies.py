import requests
from bs4 import BeautifulSoup
import xlsxwriter
import openpyxl
from requests.exceptions import MissingSchema

OG_book = openpyxl.load_workbook("cleaned_results final copy.xlsx")
OG_sheet = OG_book.active
workbook = xlsxwriter.Workbook("demo.xlsx")
worksheet = workbook.add_worksheet()
post_counter = 1
current_link = ""
current_line = 1

while post_counter < 218:
        current_link = OG_sheet['B' + str(post_counter)].value
        current_line += 1
        print(current_link)
        URL = current_link
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        #incel_replies = soup.find_all("div", class_="block-body js-replyNewMessageContainer")
        #incel_replies = soup.find_all("div", class_="message-content js-messageContent")
        incel_replies = soup.find_all("article", class_="message-body js-selectToQuote")
        clean_replies = []

        for reply in incel_replies:
            #print(reply)
            if reply.find("blockquote", class_="bbCodeBlock bbCodeBlock--expandable bbCodeBlock--quote js-expandWatch"):
                #print(reply.text.strip() + '!!')
                clean_reply = reply.text.strip()[reply.text.strip().index("Click to expand...") + 18:]
                clean_replies.append(clean_reply)
            else:
                #print(reply.text.strip() + "###")
                clean_replies.append(reply.text.strip())
            #print('-------' + '\n')

        #print(clean_replies[1:])

        worksheet.write("A" + str(current_line), URL)
        current_line += 1
        replies_len = len(clean_replies)
        replies_counter = 0
        for cleaned in clean_replies:
            #print(cleaned, "\n----")
            worksheet.write("B" + str(current_line), cleaned)
            replies_counter += 1
            current_line += 1

        post_counter += 1


workbook.close()








