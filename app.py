""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

data = {
    'item1': {'title': 'ЗАПУСК ВСЕХ ТЕСТОВ СРАЗУ', 'path': './scriptsh/runhosting_all.sh'},
}


@app.route("/whois")
def run_whois():
    """ Эта функция запуская и отвечает за тесты страницы whois. """

    cmd = ["./scriptsh/runwhois.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('report.html', text=out, json=out)


@app.route("/runapi")
def run_api():
    """ Эта функция запуская и отвечает за api тесты. """

    cmd = ["./scriptsh/runapi.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('report.html', text=out, json=out)


@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('report.html', text=out, json=out)


@app.route('/')
def welcome():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """

    return render_template('welcome.html')  # render a template


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Эта функция запуская и отвечает за процесс входа. """

    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('swooo'))
    return render_template('login.html', error=error)


@app.route("/swooo", methods=["GET", "POST"])
def show_hi():
    """ Эта функция запуская и отвечает за процесс мультивыбора в форме. """

    if request.method == "GET":
        return render_template("dubl.html", data=data)
    else:
        if request.form:
            print('start')
            for item in request.form.to_dict(flat=False)['multivubor[]']:
                print(data[item]['path'])

                with subprocess.Popen(data[item]['path'], stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      universal_newlines=True) as result:
                    out = result.communicate()
                print(out)
        return render_template("runhosting.html", data=data, text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)
