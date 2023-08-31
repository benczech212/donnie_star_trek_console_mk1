Donnie Star-Trek Console Mk1
Overview
The Donnie Star-Trek Console Mk1 is a Raspberry Pi Pico-powered light control panel inspired by the Star Trek universe. It features three different light zones ("Left Panel," "Prism," and "Right Panel") controlled by momentary buttons. Each zone can be in one of several modes such as "Solid," "Blinking," "Fade in/out," and "Random."

Features
Three independent light zones.
Each zone has multiple modes:
Off
Solid Color
Blinking
Fade in/out
Random color flicker
Mode change with momentary buttons.
Written in CircuitPython for easy modification and upgrades.
Requirements
Raspberry Pi Pico
NeoPixel strips
Momentary push buttons
Resistor and capacitors for button debouncing (optional)
Power supply compatible with NeoPixel voltage and current requirements
Hardware Setup
Connect the data inputs of the NeoPixel strips to GP0, GP1, and GP2 on the Raspberry Pi Pico.
Connect the momentary buttons to GP16, GP17, and GP18 on the Pico.
Connect all ground wires to a common ground on the Pico.
Software Setup
Install CircuitPython on your Raspberry Pi Pico following the instructions here.
Upload the main code (main.py) to your Raspberry Pi Pico.
Usage
Press the momentary button corresponding to each zone to cycle through the different light modes. The current mode will be printed to the console.

Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you'd like to change.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.