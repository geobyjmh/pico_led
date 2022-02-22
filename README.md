# Introduction
This project is used to flash Neopixels with a Raspberry Pi Pico. It takes the original code supplied to do this and refactors it to make it more usable.
# Original
From ThePiHut I purchase the  WAV-20170 (RGB Full-colour LED Matrix Panel for Raspberry Pi Pico 16x10). The example python code that came with the WAV-20170 had some indention errors I have fixed in this version. However it still has lots of commented out code, repeated code sections and areas of the code that are just not used. This project is my attempt to refactor the code.
The official online resource for the WAV-20170 can be found at [Pico RGB LED](https://www.waveshare.com/wiki/Pico-RGB-LED)
# Pico_led
This is my refactored code, it keeps the same LED patterns as the original, however the output debug print statements that were used in the original have been removed. The entry point for the code is in led.py

[YouTube video of this code in action](https://youtu.be/JlqCx8ctprE)
# bounce
A work in progress!
