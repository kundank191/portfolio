import io

def add_alarm_to_calender_events(file_in_memory, num_day_before_notif=0, num_hour_before_notif=0, num_min_before_notif=5, num_sec_before_notif=0):
    """
    function will take an .ics file from an in-memory file and then add notif to the file
    Args:
        file_in_memory : the in-memory file
        num_day_before_notif : The num days before which notif will be scheduled
        num_hour_before_notif : The num hour before which notif will be scheduled
        num_min_before_notif : The num  min before notif will be scheduled
        num_sec_before_notif : The num sec before which notif will be schedules
    """

    # Alarm Schema
    alarm_schema = f"""
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:This is an event reminder
TRIGGER:-P{num_day_before_notif}DT{num_hour_before_notif}H{num_min_before_notif}M{num_sec_before_notif}S
END:VALARM
END:VEVENT
    """

    to_replace = """END:VEVENT"""

    file_in_memory.seek(0)
    data = file_in_memory.read().decode('utf-8')

    updated_file = data.replace(to_replace, alarm_schema)

    file_in_memory.seek(0)
    file_in_memory.truncate()
    file_in_memory.write(updated_file.encode('utf-8'))

    return {"status": "success", "message": "Alarm added to the calendar events"}
