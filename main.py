import datetime

my_events = {}

def add_new_event(title, desc, date, time):
    # Checkign for time and date format
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        datetime.datetime.strptime(time, "%H:%M")
    except ValueError:
        return "Date should be YYYY-MM-DD and time HH:MM."

    # Checking for existing events with same name! Error Handling
    if title in my_events:
        return "An event with that title already exists!"

    # Add new event
    my_events[title] = {'desc': desc, 'date': date, 'time': time}
    return "Your event was added!"

def change_the_event(old_title, new_title, new_desc, new_date, new_time):
    if old_title not in my_events:
        return "Can't find that event."

    # checking the date and time format.
    try:
        datetime.datetime.strptime(new_date, "%Y-%m-%d")
        datetime.datetime.strptime(new_time, "%H:%M")
    except ValueError:
        return "Date and time format's off! Remember, YYYY-MM-DD and HH:MM."

    # Change event details
    del my_events[old_title]
    my_events[new_title] = {'desc': new_desc, 'date': new_date, 'time': new_time}
    return "Event updated!"

def show_all_events():
    # Display all existing events
    for event_title, details in sorted(my_events.items(), key=lambda x: (x[1]['date'], x[1]['time'])):
        print(f"Event: {event_title}, What's it about?: {details['desc']}, When?: {details['date']} at {details['time']}")

def delete_an_event(title):
    # Delete existinf events
    if title in my_events:
        del my_events[title]
        return "Event Deleted."
    return "No such event to delete."

def search_for_events(keyword):
    # Let's find what you're looking for!
    results = {}
    for title, info in my_events.items():
        if keyword.lower() in title.lower() or keyword.lower() in info['desc'].lower() or keyword in info['date']:
            results[title] = info
    return results

def event_manager_interface():
    # Welcome to the Event Manager! Let's manage some events!
    while True:
        print("\nWelcome to the Event Manager!")
        print("1. Add a new Event")
        print("2. Show all Events")
        print("3. Delete Event")
        print("4. Edit Event")
        print("5. Search for Events")
        print("6. Exit")
        choice = input("What would you like to do? (1-6): ")

        if choice == '1':
            title = input("Event Title: ")
            desc = input("Event Description: ")
            date = input("Date: (YYYY-MM-DD): ")
            time = input("Time? (HH:MM): ")
            print(add_new_event(title, desc, date, time))
        
        elif choice == '2':
            show_all_events()
        
        elif choice == '3':
            title = input("Which event are we saying goodbye to?: ")
            print(delete_an_event(title))

        elif choice == '4':
            old_title = input("What's the current title?: ")
            new_title = input("New title: ")
            new_desc = input("New Description?: ")
            new_date = input("New date (YYYY-MM-DD): ")
            new_time = input("And new time? (HH:MM): ")
            print(change_the_event(old_title, new_title, new_desc, new_date, new_time))

        elif choice == '5':
            keyword = input("What are you looking for? (Date, Title, Description): ")
            found_events = search_for_events(keyword)
            if found_events:
                for title, details in found_events.items():
                    print(f"Found: {title}, Details: {details['desc']} on {details['date']} at {details['time']}")
            else:
                print("Couldn't find anything like that!.")

        elif choice == '6':
            print("Goodbye! Come manage events again soon!")
            break

        else:
            print("Not sure what you mean, try a number from 1 to 6.")

# Maain execution
if __name__ == "__main__":
    event_manager_interface()
