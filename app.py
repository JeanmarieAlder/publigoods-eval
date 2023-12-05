
import json
import time
from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = 'changeit' 
Bootstrap(app)

current_start_id = 0

@app.route('/')
def index():
    all_headers = request.headers
    print(all_headers)
    for header, value in all_headers.items():
        session[header] = value
    try:
        del session['Cookie']
    except Exception as e:
        print("new session, no cookies to del.")
    print(session)
    return render_template('index.html')

@app.route('/instructions')
def instructions():
    global current_start_id
    next_id = 0
    session["name"] = request.args.get('name')
    session["timestamp_quiz_start"] = time.time()
    if session["name"] == "":
        session["name"] = "Anonymous"
    if current_start_id == 0:
        current_start_id = 1
        next_id = 0
    else:
        current_start_id = 0
        next_id = 1
    session["start_id"] = current_start_id
    return render_template('instructions.html', start_id=current_start_id, next_id=next_id, has_next=True)

@app.route('/instructions2')
def instructions2():
    prev_id = request.args.get("prev_id")
    next_id = request.args.get("next_id")
    selected_time = request.args.get("appt")
    session[f"t{prev_id}_selected_time"] = selected_time
    if selected_time == "11:15":
        session[f"t{prev_id}_correct"] = True
    else:
        session[f"t{prev_id}_correct"] = False
    session[f"t{prev_id}_end"] = time.time()
    print(session[f"t{prev_id}_end"])
    session[f"t{prev_id}_tot"] = session[f"t{prev_id}_end"] - session[f"t{prev_id}_start"]
    print("Total time in sec: " + str(session[f"t{prev_id}_tot"]))
    return render_template('instructions2.html', next_id=next_id)

@app.route('/timepicker/0')
def timepicker0():
    has_next = request.args.get("has_next")
    next_id = request.args.get("next_id")
    print(session["name"])
    session["t0_start"] = time.time()
    print(session["t0_start"])
    return render_template('timepicker0.html', has_next=has_next, next_id=next_id)

@app.route('/timepicker/1')
def timepicker1():
    has_next = request.args.get("has_next")
    next_id = request.args.get("next_id")
    session["t1_start"] = time.time()
    print(session["t1_start"])
    return render_template('timepicker1.html', has_next=has_next, next_id=next_id)

@app.route('/quizz')
def quizz():
    # Store data in a plain text file before the quizz
    with open('evaluations/before_quizz.txt', 'a') as file:
        file.write(json.dumps(dict(session)))
        file.write(",\n")
    prev_id = request.args.get("prev_id")
    selected_time = request.args.get("appt")
    session[f"t{prev_id}_selected_time"] = selected_time
    if selected_time == "11:15":
        session[f"t{prev_id}_correct"] = True
    else:
        session[f"t{prev_id}_correct"] = False
    session[f"t{prev_id}_end"] = time.time()
    session[f"t{prev_id}_tot"] = session[f"t{prev_id}_end"] - session[f"t{prev_id}_start"]
    print("Total time in sec: " + str(session[f"t{prev_id}_tot"]))
    return render_template('quizz.html')

@app.route('/thank_you', methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        for key, item in request.form.items():
            print(key)
            print(item)
            session[key] = item

    with open('evaluations/done.txt', 'a') as file:
        file.write(json.dumps(dict(session)))
        file.write(",\n")

    return render_template('thank_you.html')

# @app.route('/evaluate', methods=['POST'])
# def evaluate():
#     # Retrieve data from the form
#     selected_method = request.form.get('method')
#     feedback = request.form.get('feedback')

#     # Store data in a plain text file
#     with open('evaluations.txt', 'a') as file:
#         file.write(f'Method: {selected_method}, Feedback: {feedback}\n')

#     return 'Thank you for your feedback!'

if __name__ == '__main__':
    app.run(debug=True)
