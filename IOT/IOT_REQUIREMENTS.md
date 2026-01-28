# IoT Hardware Requirements

This project monitors electrical stability in hospital critical zones by
collecting real-time voltage and current data using IoT components.

## 1. Microcontroller
- **ESP32 (ESP-WROOM-32)**
- Supports Wi-Fi and Bluetooth
- Supports MicroPython
- Operating Voltage: 3.3V
- Used for reading sensor data and sending it to the backend

## 2. Current Sensor
- **ACS712**
- Measures AC current
- Output: Analog voltage proportional to current
- Used to detect overload conditions

## 3. Voltage Sensor
- **ZMPT101B**
- Measures AC voltage
- High accuracy isolation
- Used to detect voltage drop conditions

## 4. Power Supply
- 5V USB power supply
- Used to power ESP32

## 5. Connecting Components
- Breadboard
- Jumper wires
- USB cable
