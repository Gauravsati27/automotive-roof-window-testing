import random  # Simulating sensor data

class RoofWindowSystem:
    def __init__(self):
        self.window_open = False  # Window is initially closed
        self.temperature = 25  # Default temperature (in Celsius)
        self.rain_detected = False  # Default: No rain

    def read_sensors(self):
        """Simulate reading temperature and rain sensors"""
        self.temperature = random.randint(15, 45)  # Simulate temp between 15°C - 45°C
        self.rain_detected = random.choice([True, False])  # Simulate rain condition
    
    def control_window(self):
        """Logic for opening/closing the window"""
        if self.rain_detected:
            self.window_open = False  # Close the window if rain is detected
            print("🌧️ Rain detected! Closing the roof window.")
        elif self.temperature > 35:
            self.window_open = True  # Open window if too hot
            print("🔥 High temperature detected! Opening the roof window.")
        else:
            print("✅ Conditions normal. Window remains unchanged.")

    def display_status(self):
        """Show the current system status"""
        window_state = "OPEN" if self.window_open else "CLOSED"
        print(f"Temperature: {self.temperature}°C, Rain: {self.rain_detected}, Window: {window_state}")

# Simulating the system operation
roof_window = RoofWindowSystem()

for _ in range(5):  # Simulate 5 sensor readings
    print("\n🔄 Checking system status...")
    roof_window.read_sensors()
    roof_window.control_window()
    roof_window.display_status()
