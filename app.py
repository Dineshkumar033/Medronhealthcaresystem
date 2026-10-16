from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "medron-demo-secret-key"

CATEGORIES = [
    {"name":"Basic & Home Care","icon":"🩺"},
    {"name":"Critical Care","icon":"❤️"},
    {"name":"Respiratory & Pulmonary","icon":"🫁"},
    {"name":"Physiotherapy","icon":"🏃"},
    {"name":"Neonatal","icon":"👶"},
    {"name":"Medical Furniture & Cots","icon":"🛏️"},
    {"name":"OT Equipment","icon":"⚕️"},
    {"name":"Wheelchairs & Mobility","icon":"♿"},
    {"name":"Consumables","icon":"◉"},
]

PRODUCTS = []
for n,image in [
    ("Aneroid Sphygmomanometer", "Aneroid.png"),
    ("Body Composition Monitor", "Body Composition monitor.png"),
    ("Cholesterol Meter", "cholestrol meter.png"),
    ("Digital Thermometer", "digital thermometer.png"),
    ("Glucometer", "Glucometer.png"),
    ("Hemoglobin Meter", "Hemoglobin meter.png"),
    ("Infrared Thermometer", "Infrared.png"),
    ("Nebulizer", "Nebulizer.png"),
    ("Pulse Oximeter", "pulse oximeter.png"),
    ("Suction Machine", "Section machine.png"),
    ("Weight Scale", "Weight Scale.png"),
]:
    PRODUCTS.append({
        "name": n,
        "category": "Basic & Home Care",
        "image": f"products/Basic&Home care Equipment/{image}",
    })
for n,image in [
    ("Defibrillator", "Defibrilator.png"), ("ECG Machine", "ECG Machine.png"),
    ("Fetal Doppler", "Fetal Doppler.png"), ("Fetal Monitor", "Fetal Monitor.png"),
    ("Infusion Pump", "Infusion Pump.png"), ("Patient Monitor", "Patient Monitor.png"),
    ("Syringe Pump", "Syringer Pump.png"), ("Table Top Pulse Oximeter", "Table Top Pluse Oximeter.png"),
]:
    PRODUCTS.append({"name": n, "category": "Critical Care", "image": f"Critical care Equipments/{image}"})
for n,image in [
    ("Air Compressor", "Air compressor.png"), ("Capnograph", "Capnograph.png"),
    ("CPAP & BiPAP", "Cpap & Bipap.png"), ("Humidifier", "Humidifier.png"),
    ("ICU Ventilator", "Icu ventilator.png"), ("Oxygen Concentrator", "Oxygen Concentrator.png"),
    ("Portable Ventilator", "Portable ventilator.png"), ("Scanning Laser Therapy", "Scanning Laser Therapy.png"),
    ("Spirometer", "Spirometer.png"),
]:
    PRODUCTS.append({"name": n, "category": "Respiratory & Pulmonary", "image": f"Respiration & Pulmonory Equipments/{image}"})
for n,image in [
    ("Ankle Exercise", "Ankle Exercise 1.jpeg"), ("Ankle Motion", "Ankle motion.jpeg"),
    ("Balance Board", "Balance Board.jpeg"), ("Chest Vibrator", "chest vibrator.jpeg"),
    ("Interferential Therapy", "Interfrential therapy.jpeg"), ("IRR Lamp", "IRR lamp.jpeg"),
    ("Microwave Diathermy", "Microwave diatheramy.jpeg"), ("Multipurpose Exercise Chair", "Multipurpose exercise Chair.jpeg"),
    ("Parallel Bar", "Parallel bar (6-10).jpeg"), ("Shoulder Wheel Exercise", "Shoulder wheel Exercise.jpeg"),
    ("Static Cycle", "Static cycle.jpeg"), ("Suspension Therapy", "Suspension Therapy.jpeg"),
    ("TENS", "Tens.jpeg"), ("Tilting Table", "Tilting table.jpeg"),
    ("Ultrasound Therapy", "Ultrasound Therapy.jpeg"), ("Wax Bath", "wax Bath.jpeg"),
    ("Wobble Board", "wobble Board.jpeg"), ("Wrist Exercise", "Wrist Exercise.jpeg"),
]:
    PRODUCTS.append({"name": n, "category": "Physiotherapy", "image": f"physiotherapy Equipments/{image}"})
for n,image in [
    ("Baby Warmer", "Baby warmer.jpeg"), ("Incubator", "incubator.jpeg"), ("Phototherapy", "Phototherapy.jpeg"),
]:
    PRODUCTS.append({"name": n, "category": "Neonatal", "image": f"physiotherapy Equipments/{image}"})
for folder, category, items in [
    ("Eletrical & Manual medical cots", "Medical Furniture & Cots", [("Medical Cot 1", "cot 1.jpeg"), ("Medical Cot 2", "cot 2.jpeg"), ("Medical Cot 3", "cot 3.jpeg")]),
    ("Examination Couch", "Medical Furniture & Cots", [(f"Examination Couch {i}", f"couch {i}.jpeg") for i in range(1, 7)]),
    ("Plain Medical Cots", "Medical Furniture & Cots", [(f"Plain Medical Cot {i}", f"cot {i}.jpeg") for i in [2, 3, 4, 5, 6]] + [("Plain Medical Cot 1", "cots 1.jpeg")]),
    ("stretcher", "Medical Furniture & Cots", [(f"Stretcher {i}", f"Stertcher {i}.jpeg") for i in range(1, 7)]),
]:
    PRODUCTS.extend({"name": n, "category": category, "image": f"{folder}/{image}"} for n, image in items)

@app.context_processor
def globals(): return {"categories":CATEGORIES}

@app.route("/")
def home(): return render_template("home.html")
@app.route("/about")
def about(): return render_template("about.html")
@app.route("/products")
def products():
    selected=request.args.get("category","")
    items=PRODUCTS if not selected else [p for p in PRODUCTS if p["category"]==selected]
    return render_template("products.html",products=items,selected=selected)
@app.route("/services")
def services(): return render_template("services.html")
@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        flash("Thank you. Your message has been received.","success")
        return redirect(url_for("contact"))
    return render_template("contact.html")
@app.route("/request-quote",methods=["GET","POST"])
def quote():
    if request.method=="POST":
        flash("Thank you. Your quote request has been received.","success")
        return redirect(url_for("quote"))
    return render_template("quote.html",product_names=[p["name"] for p in PRODUCTS])
if __name__=="__main__": app.run(debug=True)
