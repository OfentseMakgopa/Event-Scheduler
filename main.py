import datetime

# Data structure to store events
events = {}

# Function to add a new event
def add_event(title, description, date, time):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        datetime.datetime.strptime(time, "%H:%M")
    except ValueError:
        return "Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."
    
    if title in events:
        return "An event with this title already exists."
    
    events[title] = {'description': description, 'date': date, 'time': time}
    return "Event added successfully."

# Function to edit an event
def edit_event(old_title, new_title, description, date, time):
    if old_title not in events:
        return "Event not found."

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        datetime.datetime.strptime(time, "%H:%M")
    except ValueError:
        return "Invalid date or time format."

    del events[old_title]
    events[new_title] = {'description': description, 'date': date, 'time': time}
    return "Event updated successfully."

# Function to list all events
def list_events():
    for title, details in sorted(events.items(), key=lambda x: (x[1]['date'], x[1]['time'])):
        print(f"Title: {title}, Description: {details['description']}, Date: {details['date']}, Time: {details['time']}")

# Function to delete an event
def delete_event(title):
    if title in events:
        del events[title]
        return "Event deleted successfully."
    else:
        return "Event not found."

# Function to search events
def search_events(search_query):
    results = {}
    for title, details in events.items():
        if search_query.lower() in title.lower() or search_query.lower() in details['description'].lower() or search_query in details['date']:
            results[title] = details
    return results

# Simple CLI for the application
def main():
    while True:
        print("\nEvent Manager")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Edit Event")
        print("5. Search Event")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            print(add_event(title, description, date, time))
        
        elif choice == '2':
            list_events()
        
        elif choice == '3':
            title = input("Enter event title to delete: ")
            print(delete_event(title))

        elif choice == '4':
            old_title = input("Enter the current title of the event: ")
            new_title = input("Enter the new title of the event: ")
            description = input("Enter the new description of the event: ")
            date = input("Enter the new event date (YYYY-MM-DD): ")
            time = input("Enter the new event time (HH:MM): ")
            print(edit_event(old_title, new_title, description, date, time))

        elif choice == '5':
            search_query = input("Enter search query (date, title or description): ")
            results = search_events(search_query)
            if results:
                for title, details in results.items():
                    print(f"Title: {title}, Description: {details['description']}, Date: {details['date']}, Time: {details['time']}")
            else:
                print("No events found matching the search criteria.")

        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
