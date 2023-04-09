from io import BytesIO
from flask import Flask, render_template, request, send_file
from calendar_optimization.calendar_api import add_alarm_to_calender_events

app = Flask(__name__, static_folder='static',
            static_url_path='', template_folder='templates')

@app.route('/')
def index():
    """
    This function will render the index page
    """

    return render_template('index.html')

@app.route('/calendar_optimization')
def calendar_optimization():
    """
    This function will render the calendar optimization page
    """
    return render_template('calendar_optimization.html')

@app.route('/update_calendar', methods=['POST'])
def update_calendar():
    """
    This function will update the calendar events with the alarm
    """
    file = request.files['file']
    file_in_memory = BytesIO()
    file.save(file_in_memory)

    # add alarm to the calendar events
    add_alarm_to_calender_events(file_in_memory)

    # return the file to the user
    file_in_memory.seek(0)
    return send_file(file_in_memory, attachment_filename=file.filename, as_attachment=True)

@app.errorhandler(404)
def page_not_found(info):
    """
    function will render the 404 page
    """
    print(info)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)
