from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages and session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_value = request.form.get('input_value')
    convert_from = request.form.get('from')
    convert_to = request.form.get('to')
    print(f"Received input: {input_value}, from: {convert_from}, to: {convert_to}")
    
    try:
        value = float(input_value)
        converted_value = value
        match convert_from:
          case "mm":
              match convert_to:
                  case "cm":
                      converted_value = value * 0.1
                  case "m":
                      converted_value = value * 0.001
                  case "km":
                      converted_value = value * 0.000001
                  case "inch":
                      converted_value = value * 0.0393701
                  case "foot":
                      converted_value = value * 0.00328084
                  case "mile":
                      converted_value = value * 0.000000621371
          case "cm":
              match convert_to:
                  case "mm":
                      converted_value = value * 10
                  case "m":
                      converted_value = value * 0.01
                  case "km":
                      converted_value = value * 0.00001
                  case "inch":
                      converted_value = value * 0.393701
                  case "foot":
                      converted_value = value * 0.0328084
                  case "mile":
                      converted_value = value * 0.00000621371
          case "m":
              match convert_to:
                  case "mm":
                      converted_value = value * 1000
                  case "cm":
                      converted_value = value * 100
                  case "km":
                      converted_value = value * 0.001
                  case "inch":
                      converted_value = value * 39.3701
                  case "foot":
                      converted_value = value * 3.28084
                  case "mile":
                      converted_value = value * 0.000621371
          case "km":
              match convert_to:
                  case "mm":
                      converted_value = value * 1000000
                  case "cm":
                      converted_value = value * 100000
                  case "m":
                      converted_value = value * 1000
                  case "inch":
                      converted_value = value * 39370.1
                  case "foot":
                      converted_value = value * 3280.84
                  case "mile":
                      converted_value = value * 0.621371
          case "inch":
              match convert_to:
                  case "mm":
                      converted_value = value * 25.4
                  case "cm":
                      converted_value = value * 2.54
                  case "m":
                      converted_value = value * 0.0254
                  case "km":
                      converted_value = value * 0.0000254
                  case "foot":
                      converted_value = value * 0.0833333
                  case "mile":
                      converted_value = value * 0.0000157828
          case "foot":
              match convert_to:
                  case "mm":
                      converted_value = value * 304.8
                  case "cm":
                      converted_value = value * 30.48
                  case "m":
                      converted_value = value * 0.3048
                  case "km":
                      converted_value = value * 0.0003048
                  case "inch":
                      converted_value = value * 12
                  case "mile":
                      converted_value = value * 0.000189394
          case "mile":
              match convert_to:
                  case "cm":
                      converted_value = value * 160934
                  case "m":
                      converted_value = value * 1609.34
                  case "km":
                      converted_value = value * 1.60934
                  case "inch":
                      converted_value = value * 0.0393701
                  case "foot":
                      converted_value = value * 0.0328084
                  case "mile":
                      converted_value = value * 0.00000198839
          case "celsius":
              match convert_to:
                  case "fahrenheit":
                      converted_value = value * 9/10 + 32
                  case "kelvin":
                      converted_value = value + 273.15
          case "fahrenheit":
              match convert_to:
                  case "celsius":
                      converted_value = (value-32) * 5/9 
                  case "kelvin":
                      converted_value = (value-32) * 5/9 + 273.15
          case "kelvin":
              match convert_to:
                  case "fahrenheit":
                      converted_value = value * 9/5 - 459.67
                  case "celsius":
                      converted_value = value - 273.15
          case "mg":
              match convert_to:
                  case "g":
                      converted_value = value * 0.001
                  case "kg":
                      converted_value = value * 0.000001
                  case "lb":
                      converted_value = value * 0.00000220462
          case "g":
              match convert_to:
                  case "mg":
                      converted_value = value * 1000
                  case "kg":
                      converted_value = value * 0.001
                  case "lb":
                      converted_value = value * 0.00220462
          case "kg":
              match convert_to:
                  case "mg":
                      converted_value = value * 1000000
                  case "g":
                      converted_value = value * 1000
                  case "lb":
                      converted_value = value * 2.20462
          case "lb":
              match convert_to:
                  case "mg":
                      converted_value = value * 453592
                  case "g":
                      converted_value = value * 453.592
                  case "kg":
                      converted_value = value * 0.453592
                  
        result = f"{value} {convert_from} is equal to {converted_value:.4f} {convert_to}"
    except ValueError:
        flash("Please enter a valid number")
        return redirect(url_for('index'))
    
    # Pass the result to the template
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
