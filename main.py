from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

user_data = {
    'name': 'Иван Иванов',
    'email': 'ivan@example.com',
    'password': 'password123'
}

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']


        user_data['name'] = name
        user_data['email'] = email
        user_data['password'] = password

        flash('Профиль успешно обновлен!')
        return redirect(url_for('index'))

    return render_template('index.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)
