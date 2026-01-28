import csv

CSV_FILE = "D:\Power Alert System\med-power-alert\data.csv"
HTML_FILE = "D:\Power Alert System\med-power-alert\dem.html"    
def check_voltage(voltage):
    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if float(row["min_voltage"]) <= voltage <= float(row["max_voltage"]):
                return row["status"], row["color"]
    return "NORMAL", "green"


# ---- USER INPUT ----
voltage = float(input("Enter present voltage: "))
current = float(input("Enter present current (A): "))

status, color = check_voltage(voltage)

# ---- MESSAGE ----
if status == "CRITICAL_LOW":
    message = "CRITICAL ⚠️ Voltage Too Low"
elif status == "WARNING_UNSTABLE":
    message = "WARNING ⚠️ Voltage Unstable"
elif status == "CRITICAL_HIGH":
    message = "CRITICAL ⚠️ Voltage Too High"
else:
    message = "NORMAL ✅ Voltage Stable"

# ---- HTML OUTPUT ----
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Voltage & Current Alert</title>
    <style>
        body {{
            font-family: Arial;
            text-align: center;
            margin-top: 50px;
        }}
        .alert-box {{
            width: 300px;
            padding: 20px;
            margin: auto;
            border-radius: 10px;
            color: white;
            font-size: 20px;
            font-weight: bold;
        }}
        .green {{ background-color: #2ecc71; }}
        .yellow {{ background-color: #f1c40f; color: black; }}
        .red {{ background-color: #e74c3c; }}
    </style>
</head>
<body>

<h2>Hospital Voltage Monitoring System</h2>

<p><b>Voltage:</b> {voltage} V</p>
<p><b>Current:</b> {current} A</p>

<div class="alert-box {color}">
    {message}
</div>

</body>
</html>
"""

with open(HTML_FILE, "w", encoding="utf-8") as file:
    file.write(html_content)

print("\n✅ Output generated successfully!")
print("👉 Open 'output.html' in your browser")