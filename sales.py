import pandas as pd
import matplotlib.pyplot as plt

def excel_to_pie_pdf(excel_file, pdf_file):
    # Read data from Excel
    df = pd.read_excel(r"C:\Users\DELL\Downloads\sales.xlsx")
    
    # Make pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(df['Sales'], labels=df['Item'], autopct='%1.1f%%', startangle=90)
    plt.title("Sales_Analysis")
    
    # Save chart directly as PDF
    plt.savefig(pdf_file)
    plt.close()

# Run function
excel_to_pie_pdf("sales.xlsx", "sales_chart.pdf")
