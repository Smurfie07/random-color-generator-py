from flask import Flask, render_template
import random
import os
app = Flask(__name__)
rgb = (
    os.environ.get("DEFAULT_COLOR")
    if os.environ.get("DEFAULT_COLOR")
    else (0, 128, 128)
    )
@app.route("/")
def randColorGen():
    rgb = (
        random.randint(0,255), 
        random.randint(0,255),
        random.randint(0,255),
        )
    rgbFormula = "rgb" + str(rgb)
    return render_template(
        "main.html",
        color = rgbFormula,
    )

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0", 
        port = 520,
        )