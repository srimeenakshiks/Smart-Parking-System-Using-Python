import random
import time

# Function to read car details from cardetails.txt
def read_car_details():
    with open("cardetails.txt", "r") as file:
        return [line.strip() for line in file]

# Function to read parking spaces from parking.txt
def read_parking_spaces():
    with open("parking.txt", "r") as file:
        return [line.strip() for line in file]

# Function to write event to the database
def write_to_database(event):
    with open("database.txt", "a") as file:
        file.write(event + "\n")

# Simulate car details and parking spaces
car_details = read_car_details()
parking_spaces = read_parking_spaces()

def simulate_car_presence():
    while True:
        # Randomly select a car and parking spot
        selected_car = random.choice(car_details)
        selected_spot = random.choice(parking_spaces)

        # Simulate a car entering the parking spot
        enter_event = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Car entered {selected_spot}: {selected_car}"
        print(enter_event)
        write_to_database(enter_event)

        time.sleep(1)  # Simulate detection time

        # Simulate a car leaving the parking spot
        exit_event = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Car left {selected_spot}: {selected_car}"
        print(exit_event)
        write_to_database(exit_event)

        time.sleep(random.uniform(1, 4))

# Start simulation
simulate_car_presence()
