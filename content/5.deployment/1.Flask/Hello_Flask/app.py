from flask import Flask, render_template_string, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template_string('''
    <head>My Salary Calculator</head>
    <form action="/" method="post">
    <p>Salary: <input type="number" name="salary" value="" id="val1"></p>
    <p>Bonus: <input type="number" name="bonus" value="" id="val2"></p>
    <p>Tax: <input type="number" name="tax" value="" id="val3"></p>
    <input type="submit" value="Calculate" id="button_calculate">
    <p>Salary after tax: <input type="number" name="result_dc" value="" id="result"></p>
</form>
<script>
    var val1_input = document.getElementById("val1");
    var val2_input = document.getElementById("val2");
    var val3_input = document.getElementById("val3");
    var result_input = document.getElementById("result");
    var button_input = document.getElementById("button_calculate");
    button_input.onclick = function (event) {
        result_input.value = parseFloat(val1_input.value) + parseFloat(val2_input.value) - parseFloat(val3_input.value);
        //event.preventDefault(); // don't send to server
        return false; // don't send to server
    }
</script>
''')


if __name__ == "__main__":
    app.run(debug=True)