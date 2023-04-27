import pandas as pd
import openai
from config import CHATGPT_KEY
# ChatGPT recommendations below; see the store_summary() for explanation:
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from datetime import date

openai.api_key = CHATGPT_KEY


def read_file(file):
    """
    Retrieves the ChatGPT summaries and adds them all to a single string variable

    Returns a string variable
    """
    punctuation = ","
    final_rows = []
    file = pd.read_csv(file, delimiter=punctuation, header=None) # used ChatGPT to learn about delimiter
    for row_number, row in file.iterrows():
        line_text = ""
        for text in row:
            line_text = line_text + str(text) + punctuation
        line_text = line_text[:-1]
        final_rows.append(line_text)
    final_text = "\n".join(final_rows)
    return final_text


def summarize(text):
    """
    Uses ChatGPT API to summarize the contents of a string text entry

    Returns the generated newsarticle
    """
    prompt = "Summarize the following summaries in an unbiased newsarticle format. Keep it sylistically consistent" + text
    summary = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    summary = summary["choices"][0]["message"]["content"]
    return summary


def store_summary(text, file):
    """
    Builds the newsarticle content as a PDF file using desired formatting
    """
    # ChatGPT used extensively to discover this method of converting to PDF and then stylizing text in the specific way I wanted. Required incremental testing/debugging.
    file = SimpleDocTemplate(file, pagesize=letter)
    header = ParagraphStyle(name="center", alignment=1, fontName="Helvetica-Bold")
    title = Paragraph("Weekly Recall Summary Generated on " + str(date.today()) +":", header)
    body_style = getSampleStyleSheet()["Normal"]
    body_style.firstLineIndent = inch/2
    body_style.spaceBefore = 12
    body = Paragraph(text, body_style)
    footer_style = getSampleStyleSheet()["Normal"]
    footer_style.firstLineIndent = inch/2
    footer = Paragraph("The previous summary was generated using ChatGPT based on analysis of relevant recalls.", footer_style)
    file.build([title, body, footer])
    # I tried the following methods before landing on this code:
    # 1. Conversion to pdf using less modules. I encountered a bug/feature where the entire text would write on the first line. No newlines, so could not read the output
    # 2. Conversion to docx then to pdf. Conversion to docx worked in 3 lines of code. Conversion to pdf required word installation/libretexts - not portable
    # 3. Conversion to html then to pdf. Made good progress, but was not happy with design and wanted to keep most of the code in Python


def newsarticle_creation(file):
    """
    Reads a database CSV file, uses ChatGPT to summarize the variable and output to new file

    Prints a notification that all entries have generated
    """
    print("Generating the newspaper:")
    newsarticle = read_file(file)
    newsarticle = summarize(newsarticle)
    store_summary(newsarticle, "demo_newspaper.pdf")
    print("Newspaper generated")


def main():
    database = "demo_summaries.csv"
    newsarticle_creation(database)


if __name__ == "__main__":
    main()
