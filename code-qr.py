from flask import Flask, request, redirect, render_template_string
import csv
import qrcode
import os

app = Flask(__name__)

# Path to store CSV data
CSV_FILE = "submissions.csv"

# HTML form template with mobile responsiveness
FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Access StudyBuddy</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e6f2ff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 15px;
        }
        .form-container {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            box-sizing: border-box;
        }
        h2 {
            text-align: center;
            color: #0066cc;
            margin-bottom: 20px;
        }
        label {
            font-weight: bold;
            color: #004080;
            display: block;
            margin-bottom: 6px;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"] {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 1px solid #99ccff;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 16px;
        }
        button {
            background-color: #3399ff;
            color: white;
            padding: 12px;
            width: 100%;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2673cc;
            cursor: pointer;
        }
        /* Smaller screen adjustments */
        @media (max-width: 480px) {
            h2 {
                font-size: 20px;
            }
            input, button {
                font-size: 14px;
                padding: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Enter Your Details to Proceed</h2>
        <form method="post">
            <label>Full Name:</label>
            <input type="text" name="fullname" required>
            
            <label>Email:</label>
            <input type="email" name="email" required>
            
            <label>Phone Number:</label>
            <input type="tel" name="phone" required>
            
            <button type="submit">Submit & Proceed</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        phone = request.form.get("phone")
        
        # Save to CSV
        file_exists = os.path.isfile(CSV_FILE)
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Full Name", "Email", "Phone"])
            writer.writerow([fullname, email, phone])
        
        # Redirect to StudyBuddy site
        return redirect("https://www.studybuddy.africa/")
    
    return render_template_string(FORM_HTML)

def generate_qr(server_url):
    img = qrcode.make(server_url)
    img.save("my-qrcode.png")
    print(f"QR Code generated and saved as 'my-qrcode.png'. Link: {server_url}")

if __name__ == "__main__":
    # Set your server address here for QR generation
    server_url = "https://qrcode-scanner-8d9g.onrender.com"
    generate_qr(server_url)
    app.run(debug=True)
