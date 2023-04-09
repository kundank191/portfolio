def add_alarm_to_calender_events(filepath, num_day_before_notif=0, num_hour_before_notif=0, num_min_before_notif=5, num_sec_before_notif=0):
    """
    function will take an .ics file and then add notif to the file
    Args:
        filepath : the location of the file
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

    with open(filepath, "r", encoding="utf-8") as file:
        data = file.read()

    updated_file = data.replace(to_replace, alarm_schema)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(updated_file)

    return {"status": "success", "message": "Alarm added to the calendar events"}