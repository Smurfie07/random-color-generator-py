from flask import Flask, render_template
import random

app = Flask(__name__)
rgb = (0, 0, 0)
@app.route("/")
def randColorGen():
    rgb = (random.randint(0,255), 
           random.randint(0,255),
           random.randint(0,255),)
    rgbFormula = "rgb" + str(rgb)
    return render_template(
        "main.html",
        color = rgbFormula,
    )

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0", 
        port = 520,
        debug= True,
        )