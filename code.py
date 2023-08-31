import board
import neopixel
import time
import random
import digitalio

class EffectManager:
    def __init__(self, pin, num_pixels, button_pin, name):
        self.strip = neopixel.NeoPixel(pin, num_pixels, auto_write=False)
        self.button = digitalio.DigitalInOut(button_pin)
        self.button.direction = digitalio.Direction.INPUT
        self.button.pull = digitalio.Pull.UP
        self.mode_list = ['off', 'solid', 'blinking', 'fade', 'random']
        self.current_mode = -1  # Will be set to 0 on the first button press
        self.fade_value = 0
        self.fade_direction = 1  # 1 for increasing brightness, -1 for decreasing
        self.solid_color = (255, 0, 0)
        self.name = name  # Name of the zone
        self.prev_button_state = True  # Initially released

    def check_button(self):
        current_button_state = self.button.value
        if self.prev_button_state and not current_button_state:
            # Button was just pressed
            pass
        elif not self.prev_button_state and current_button_state:
            # Button was just released
            self.next_mode()
        self.prev_button_state = current_button_state

    def next_mode(self):
        self.current_mode = (self.current_mode + 1) % len(self.mode_list)
        print(f"{self.name} is now in {self.mode_list[self.current_mode]} mode.")
        time.sleep(0.3)  # Simple debounce

    def run_effect(self):
        self.check_button()
        mode = self.mode_list[self.current_mode]
        
        if mode == 'off':
            self.strip.fill((0, 0, 0))
        elif mode == 'solid':
            self.strip.fill(self.solid_color)
        elif mode == 'blinking':
            if int(time.time()) % 2 == 0:
                self.strip.fill(self.solid_color)
            else:
                self.strip.fill((0, 0, 0))
        elif mode == 'fade':
            self.fade_value += self.fade_direction * 5
            if self.fade_value > 255 or self.fade_value < 0:
                self.fade_direction *= -1
            self.strip.fill((self.fade_value, 0, 0))
        elif mode == 'random':
            for i in range(len(self.strip)):
                self.strip[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        self.strip.show()

# Initialize Effect Managers
left_panel = EffectManager(board.GP0, 10, board.GP16, "Left Panel")
prism = EffectManager(board.GP1, 10, board.GP17, "Prism")
right_panel = EffectManager(board.GP2, 10, board.GP18, "Right Panel")

# Simulate button press to set initial modes
left_panel.next_mode()
prism.next_mode()
right_panel.next_mode()

while True:
    # Run effects based on current modes
    left_panel.run_effect()
    prism.run_effect()
    right_panel.run_effect()

    time.sleep(0.1)  # Pause for a bit
