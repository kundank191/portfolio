from os import environ
from io import BytesIO
from flask import Flask, render_template, request, send_file
from calendar_optimization.calendar_api import add_alarm_to_calender_events
from pdf_editor import crop_pdf
from database.db import Project
from mongoengine import connect

app = Flask(
    __name__, 
    static_folder='static',
    static_url_path='', 
    template_folder='templates'
)

connect(host = environ.get('MONGO_URI'))

@app.route('/')
def index():
    """
    This function will render the index page
    """
    projects = Project.objects()
    return render_template('index.html', projects = projects)

@app.route('/projects/calendar_optimization')
def calendar_optimization():
    """
    This function will render the calendar optimization page
    """
    return render_template('calendar_optimization.html')

@app.route('/projects/crop_pdf')
def crop_pdf():
    """
    This function will render the crop pdf page
    """
    return render_template('crop_pdf.html')

@app.route('/handle_crop_pdf', methods=['POST'])
def handle_crop_pdf():
    file = request.files['file']
    left = int(request.form['left'])
    top = int(request.form['top'])
    width = int(request.form['width'])
    height = int(request.form['height'])

    file_in_memory = BytesIO()
    file.save(file_in_memory)

    cropped_pdf = crop_pdf(file_in_memory, left, top, width, height)

    return send_file(cropped_pdf, mimetype='application/pdf', as_attachment=True, attachment_filename='cropped_pdf.pdf')

@app.route('/update_calendar', methods=['POST'])
def update_calendar():
    """
    This function will update the calendar events with the alarm
    """
    file = request.files['file']
    num_day_before_notif = int(request.form.get('num_day_before_notif', 0))
    num_hour_before_notif = int(request.form.get('num_hour_before_notif', 0))
    num_min_before_notif = int(request.form.get('num_min_before_notif', 5))
    num_sec_before_notif = int(request.form.get('num_sec_before_notif', 0))

    file_in_memory = BytesIO()
    file.save(file_in_memory)

    # add alarm to the calendar events
    add_alarm_to_calender_events(file_in_memory, num_day_before_notif, num_hour_before_notif, num_min_before_notif, num_sec_before_notif)

    # return the file to the user
    file_in_memory.seek(0)
    return send_file(file_in_memory, download_name=file.filename, as_attachment=True)

@app.errorhandler(404)
def page_not_found(info):
    """
    function will render the 404 page
    """
    print(info)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)
