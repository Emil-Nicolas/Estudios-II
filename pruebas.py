from Act3 import hoja_otros
import openpyxl
wb = openpyxl.load_workbook("exel.xlsx")
wb.save("exel.xlsx")

cabecera = hoja_otros.append(["Pais", "Oros", "Platas", "Bronces"])
hoja_otros.move_range("A7:D7", rows=-6, cols=0)