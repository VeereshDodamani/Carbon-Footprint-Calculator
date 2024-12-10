from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_footprint():
    if request.method == 'POST':
        # Get user input from the form
        energy_consumption = float(request.form['energy_consumption'])  # in kWh
        transportation = float(request.form['transportation'])  # in km per week
        waste_generated = float(request.form['waste_generated'])  # in kg per week

        # Calculate carbon footprint (this is a simple approximation)
        energy_footprint = energy_consumption * 0.92  # Assume 0.92 kg CO2 per kWh
        transportation_footprint = transportation * 0.19  # Assume 0.19 kg CO2 per km (average car)
        waste_footprint = waste_generated * 0.5  # Assume 0.5 kg CO2 per kg of waste

        total_footprint = energy_footprint + transportation_footprint + waste_footprint

        return render_template('index.html', footprint=total_footprint)

    return render_template('index.html', footprint=None)


if __name__ == '__main__':
    app.run(debug=True)
