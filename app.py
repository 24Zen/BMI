from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    yourbmi = None
    category = ""

    if request.method == "POST":
        # รับค่า weight และ height จากฟอร์ม
        a = float(request.form["weight"])
        b = float(request.form["height"])

        # คำนวณ BMI
        yourbmi = a / (b ** 2)

        # Debugging: Print BMI in the terminal
        print(f"Your BMI is: {yourbmi:.2f}")

 # กำหนด category ตามค่าของ BMI
        if yourbmi < 18.5:
            category = f"Your weight is less than 18.5: {yourbmi:.2f}"
        elif 18.5 <= yourbmi < 25:
            category = f"Your weight is less than 25 so perfect boby : {yourbmi:.2f}"
        elif 25 <= yourbmi < 30:
            category = f"Your weight is more than 30 chuby girl :  {yourbmi:.2f}"
        elif 30 <= yourbmi < 35:
            category = f"Your weight is more than 35, Ok you fatty : {yourbmi:.2f}"
        elif 35 <= yourbmi < 40:
            category = f"Dangerous : {yourbmi:.2f}"
        else:
            category = f"More than 40 go to hospital : Your BMI is {yourbmi:.2f}, seek medical!"

    return render_template("index.html", yourbmi=yourbmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
    