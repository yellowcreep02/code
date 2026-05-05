import win32com.client as win32
from datetime import datetime

# ====== 第一部分：假装这是你从仪器读回来的数据 ======
product_name = "PA_Module_V2"
test_date = datetime.now().strftime("%Y-%m-%d %H:%M")

# 假装测了5个频点的增益（单位dB）
freq_list = [800, 1200, 2000, 3500, 5800]       # MHz
gain_list = [12.3, 12.5, 12.1, 11.8, 11.2]      # dB

# 合格标准
gain_min = 10.0
gain_max = 14.0

# ====== 第二部分：自动判定 ======
print(f"产品: {product_name}")
print(f"测试时间: {test_date}")
print("-" * 40)

all_pass = True
for freq, gain in zip(freq_list, gain_list):
    if gain_min <= gain <= gain_max:
        result = "PASS"
    else:
        result = "FAIL"
        all_pass = False
    print(f"  {freq} MHz → 增益 {gain} dB → {result}")

print("-" * 40)
print(f"总判定: {'PASS' if all_pass else 'FAIL'}")

# ====== 第三部分：自动写入Excel ======
excel = win32.DispatchEx('excel.application')
wb = excel.Workbooks.Add()
ws = wb.worksheets(1)
ws.name = "测试报告"

# 写表头
ws.Range('A1').value = '产品型号'
ws.Range('B1').value= product_name
ws.Range('A2').value= '测试时间'
ws.Range('B2').value= test_date
ws.Range('A4').value= '频率(MHz)'
ws.Range('B4').value= '增益(dB)'
ws.Range('C4').value= '判定'

# 写数据
for i, (freq, gain) in enumerate(zip(freq_list, gain_list)):
    row = i + 5
    ws.Range(f'A{row}').value = freq
    ws.Range(f'B{row}').value = gain
    ws.Range(f'C{row}').value = 'PASS' if gain_min <= gain <= gain_max else 'FAIL'

# 写总判定
last_row = len(freq_list) + 5
ws.Range(f'A{last_row}').value = '总判定'
ws.Range(f'B{last_row}').value = 'PASS' if all_pass else 'FAIL'

# 保存
file_path = r'C:\Users\35382\Desktop\test_data.xlsx'
wb.SaveAs(file_path)
wb.Close()
excel.Quit()
print(f"\n报告已保存: test_report.xlsx")
