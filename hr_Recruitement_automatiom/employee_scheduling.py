# Add Schedule Entries
schedules = []   

# prevent double-booking
def time_to_minutes(time_str):
    """Convert 'HH:MM' string to total minutes."""
    hours, minutes = map(int, time_str.split(":"))          # map() helps apply a function (here int()) to every item in an iterable (like a list).
    return hours * 60 + minutes

def shifts_overlap(shift1, shift2):
    """Check if two shifts overlap.
    
    Each shift is a string like '09:00-17:00'.
    """
    start1, end1 = shift1.split("-")
    start2, end2 = shift2.split("-")
    
    start1_min = time_to_minutes(start1)                    # end1_min <= start2_min means: shift 1 ends before or exactly when shift 2 starts — no overlap here.
    end1_min = time_to_minutes(end1)                        # end2_min <= start1_min means: shift 2 ends before or exactly when shift 1 starts — also no overlap.
    start2_min = time_to_minutes(start2)
    end2_min = time_to_minutes(end2)
    
    return not (end1_min <= start2_min or end2_min <= start1_min)       # with not it returns True meaning no overlap, what we want is return false to indicate overlap

def add_schedule(schedules, employee_id, date, shift):
 
 # Check for double booking
    for schedule in schedules:
        if schedule["employee_id"] == employee_id and schedule["date"] == date:
            if shifts_overlap(schedule["shift"], shift):
                print(f"Error: Employee {employee_id} already has an overlapping shift on {date}.")
                return
    
    # No overlap, add schedule
    schedule = {
        "employee_id": employee_id,
        "date": date,
        "shift": shift
    }
    
    schedules.append(schedule)
    print(f"Schedule added for employee {employee_id} on {date} for {shift}.")

# View Schedules by Employee id
def view_schedules_for_employee(schedules, employee_id):
    found = False
    for schedule in schedules:
        if schedule["employee_id"] == employee_id:
            print(schedule)
            found = True
    if not found:
        print(f"No schedules found for employee {employee_id}.")

# View Schedules on a Specific Date
def view_schedules_for_date(schedules, date):
    found = False
    for schedule in schedules:
        if schedule["date"] == date:
            print(schedule)
            found = True
    if not found:
        print(f"No schedules found for {date}.")

# Update an employee’s shift for a specific date:
def update_schedule(schedules, employee_id, date, new_shift):
    for schedule in schedules:
        if schedule["employee_id"] == employee_id and schedule["date"] == date:
            schedule["shift"] = new_shift
            print(f"Schedule updated for employee {employee_id} on {date}.")
            return
    print(f"No schedule found for employee {employee_id} on {date}.")


# remove schdule
def remove_schedule(schedules, employee_id, date):
    for i, schedule in enumerate(schedules):
        if schedule["employee_id"] == employee_id and schedule["date"] == date:
            del schedules[i]
            print(f"Schedule for employee {employee_id} on {date} removed.")
            return
    print(f"No schedule found for employee {employee_id} on {date}.")


add_schedule(schedules, 101, "2025-08-02", "09:00-13:00")
add_schedule(schedules, 101, "2025-08-02", "12:00-18:00")
add_schedule(schedules, 101, "2025-08-02", "14:00-18:00")