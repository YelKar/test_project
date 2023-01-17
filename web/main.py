from datetime import datetime

from flask import Flask, render_template
import qrcode

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("qr.html", qr_src="png.png")


@app.route("/qr/<int:data>")
def gen_qr_int(data):
    filename = datetime.now().strftime(f"qr_int{data}.png")
    img = qrcode.make(data)
    img.save(f"static/QRcodes/{filename}")
    return render_template("qr.html", qr_src=filename)


@app.route("/qr/<string:data>")
def gen_qr(data):
    filename = datetime.now().strftime(f"qr{data}.png")
    img = qrcode.make(data)
    img.save(f"static/QRcodes/{filename}")
    return render_template("qr.html", qr_src=filename)


app.run(debug=True)
