import openpyxl
import openpyxl
from openpyxl.chart import BarChart,Reference

wb = openpyxl.load_workbook("exel.xlsx")

sheet = wb.active
for i in range(10):
    sheet.append([i])

values = Reference(sheet, min_col=5, min_row=2,
                   max_col=5, max_row=7)

chart = BarChart()
chart.add_data(values)
chart.title = " Medallas olimpicas "
chart.x_axis.title = " X_AXIS "
chart.y_axis.title = " Y_AXIS "
sheet.add_chart(chart, "E2")
wb.save("barChart.xlsx")

print("GRAFICA GENERADA")