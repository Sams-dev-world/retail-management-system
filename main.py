from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def loginPage():
    return render_template('login.html')

@app.route("/homepage")
def homePage():
    return render_template('homepage.html')

@app.route('/inventory')
def inventoryPage():
    return render_template('inventory.html')

@app.route('/sales_history')
def salesHistory():
    return render_template('sales_hist.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')


if __name__ == '__main__':
    app.run(debug=True)