# test_roof_window.py

from roof_window import RoofWindowSystem

def test_window_closes_when_rain_detected():
    """
    Test that the window closes when rain is detected.
    """
    system = RoofWindowSystem()
    # Set up conditions: simulate rain and any temperature value
    system.rain_detected = True
    system.temperature = 30  # arbitrary value
    system.window_open = True  # Assume window might be open
    system.control_window()   # Apply the control logic
    assert system.window_open == False, "Window should be closed when rain is detected."

def test_window_opens_when_high_temperature_and_no_rain():
    """
    Test that the window opens when the temperature is high and there's no rain.
    """
    system = RoofWindowSystem()
    # Set up conditions: high temperature and no rain
    system.rain_detected = False
    system.temperature = 40  # above the threshold (35°C)
    system.window_open = False  # Assume window starts closed
    system.control_window()     # Apply the control logic
    assert system.window_open == True, "Window should be open when temperature is high and no rain."

def test_window_remains_unchanged_under_normal_conditions():
    """
    Test that the window state remains unchanged under normal conditions.
    """
    system = RoofWindowSystem()
    # Set up conditions: normal temperature and no rain
    system.rain_detected = False
    system.temperature = 25  # normal temperature
    # Let's assume window starts closed; the control logic should not change it.
    system.window_open = False  
    system.control_window()   # Apply the control logic
    # Under normal conditions, no action is taken (window remains closed)
    assert system.window_open == False, "Window state should remain unchanged under normal conditions."
