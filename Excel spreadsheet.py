import openpyxl as xl

wb = xl.load_workbook('transactions.xlxs')
sheet = wb['Sheet1']