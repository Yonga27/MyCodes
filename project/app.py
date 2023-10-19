from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.static_folder = 'static'

student_attendance = {}

@app.route('/')
def index():
    return render_template('index.html', students=student_attendance)

@app.route('/mark_attendance', methods=["POST"])
def mark_attendance():
    student_name = request.form["student_name"]
    attendance_status = request.form["attendance_status"]
    student_attendance[student_name] = attendance_status
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
