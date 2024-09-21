import datetime

# Sample employee data
employees = {
    1: {'name': 'Alice', 'hourly_rate': 20, 'hours_worked': 0},
    2: {'name': 'Bob', 'hourly_rate': 25, 'hours_worked': 0},
}

attendance_records = {}

def clock_in(employee_id):
    """Record the clock-in time for an employee."""
    now = datetime.datetime.now()
    attendance_records[employee_id] = {'clock_in': now, 'clock_out': None}
    print(f"{employees[employee_id]['name']} clocked in at {now.strftime('%Y-%m-%d %H:%M:%S')}.")

def clock_out(employee_id):
    """Record the clock-out time and calculate hours worked."""
    now = datetime.datetime.now()
    if employee_id in attendance_records and attendance_records[employee_id]['clock_out'] is None:
        attendance_records[employee_id]['clock_out'] = now
        clock_in_time = attendance_records[employee_id]['clock_in']
        hours_worked = (now - clock_in_time).seconds / 3600
        employees[employee_id]['hours_worked'] += hours_worked
        print(f"{employees[employee_id]['name']} clocked out at {now.strftime('%Y-%m-%d %H:%M:%S')}.")

        # Calculate pay
        pay = hours_worked * employees[employee_id]['hourly_rate']
        print(f"Total pay for {employees[employee_id]['name']}: ${pay:.2f}")
    else:
        print("Error: Employee has not clocked in or has already clocked out.")

def view_attendance():
    """Display attendance records."""
    for employee_id, record in attendance_records.items():
        name = employees[employee_id]['name']
        clock_in_time = record['clock_in'].strftime('%Y-%m-%d %H:%M:%S')
        clock_out_time = record['clock_out'].strftime('%Y-%m-%d %H:%M:%S') if record['clock_out'] else "Still Clocked In"
        print(f"{name}: Clocked In at {clock_in_time}, Clocked Out at {clock_out_time}")

def main():
    while True:
        print("\n1. Clock In")
        print("2. Clock Out")
        print("3. View Attendance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            employee_id = int(input("Enter Employee ID: "))
            if employee_id in employees:
                clock_in(employee_id)
            else:
                print("Invalid Employee ID.")
        elif choice == '2':
            employee_id = int(input("Enter Employee ID: "))
            if employee_id in employees:
                clock_out(employee_id)
            else:
                print("Invalid Employee ID.")
        elif choice == '3':
            view_attendance()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
