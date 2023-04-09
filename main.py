from flask import Flask, render_template, request, send_from_directory
import constants
from calendar_optimization.calendar_api import add_alarm_to_calender_events

app = Flask(__name__, static_folder='static',
            static_url_path='', template_folder='templates')

@app.route('/')
def index():
    """
    This function will render the index page
    """

    return render_template('index.html')


@app.route('/update_calendar', methods=['POST'])
def update_calendar():
    """
    This function will update the calendar events with the alarm
    """
    file_name = request.files['file']
    file_name.save(constants.LOCATION_TO_SAVE_FILES + file_name.filename)

    # add alarm to the calendar events
    add_alarm_to_calender_events(
        constants.LOCATION_TO_SAVE_FILES + file_name.filename)

    # return the file to the user
    return send_from_directory(constants.LOCATION_TO_SAVE_FILES,
                               file_name.filename,
                               as_attachment=True)

@app.errorhandler(404)
def page_not_found(info):
    """
    function will render the 404 page
    """
    print(info)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)