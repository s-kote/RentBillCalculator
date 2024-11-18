from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # รับข้อมูลจากฟอร์ม
        room_rent = int(float(request.form['room_rent']))  # แปลงเป็น int
        # ตรวจสอบค่าส่วนกลาง
        if request.form['common_fee_select'] == 'custom':
            common_fee = int(float(request.form['common_fee']))  # แปลงเป็น int
        else:
            common_fee = int(float(request.form['common_fee_select']))  # แปลงเป็น int

        # ตรวจสอบอัตราค่าไฟฟ้า
        if request.form['electricity_rate_select'] == 'custom':
            electricity_rate = int(float(request.form['electricity_rate']))  # แปลงเป็น int
        else:
            electricity_rate = int(float(request.form['electricity_rate_select']))  # แปลงเป็น int

        # ตรวจสอบอัตราค่าน้ำ
        if request.form['water_rate_select'] == 'custom':
            water_rate = int(float(request.form['water_rate']))  # แปลงเป็น int
        else:
            water_rate = int(float(request.form['water_rate_select']))  # แปลงเป็น int

        meter_electricity_last_month = int(float(request.form['meter_electricity_last_month']))  # แปลงเป็น int
        meter_electricity_this_month = int(float(request.form['meter_electricity_this_month']))  # แปลงเป็น int
        meter_water_last_month = int(float(request.form['meter_water_last_month']))  # แปลงเป็น int
        meter_water_this_month = int(float(request.form['meter_water_this_month']))  # แปลงเป็น int

        # คำนวณค่าไฟ
        meter_electricity_used = meter_electricity_this_month - meter_electricity_last_month
        electricity_cost = meter_electricity_used * electricity_rate

        # คำนวณค่าน้ำ
        meter_water_used = meter_water_this_month - meter_water_last_month
        water_cost = meter_water_used * water_rate

        # คำนวณยอดรวม
        total_amount = room_rent + electricity_cost + water_cost + common_fee

        return render_template('result.html', room_rent=room_rent, electricity_cost=int(electricity_cost),
                               water_cost=int(water_cost), common_fee=common_fee, total_amount=int(total_amount),
                               meter_electricity_used=meter_electricity_used,
                               meter_water_used=meter_water_used,
                               meter_electricity_this_month=meter_electricity_this_month,
                               meter_electricity_last_month=meter_electricity_last_month,
                               meter_water_this_month=meter_water_this_month,
                               meter_water_last_month=meter_water_last_month)

    return render_template('form.html')
