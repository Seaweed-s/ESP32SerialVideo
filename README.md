# ESP32SerialVideo
A way to get video from an ESP32 over USB using serial, primarily developed for integration with [EyeTrackVR](https://github.com/RedHawk989/EyeTrackVR).

This repository contains my implementation of wired video tranfer for the ESP32. I made this because most of the other methods I've seen to get video from the ESP32 to a PC is using WiFi which I did not want to use.

## Capabilities
In the current configuration I'm able to achieve a frame rate of approximately 17-20 FPS with a 240x240 grayscale video feed.
To achieve this I'm currently using a baud rate of 2 million, which I have tested to be stable with two ESP32 CAMs connected to the same USB 3.0 hub.
Through my testing, I found that 3 million baud is possible when using a single ESP32 on a USB hub and, when plugged into PC front-panel IO, baud rates can barely exceed ~500 thousand.

## Purpose
The primary purpose for this project was to implement it into [EyeTrackVR](https://github.com/RedHawk989/EyeTrackVR), allowing me to use the USB port in my VR headset to power the ESP32s and get data from the ESP32s instead of through WiFi.

## Included in this repository
The firmware for the ESP32s was writted using platformio in VScode and as such that is the format the ESP Firmware folder takes.
The python program is a simple example program that I wrote to read and decode the incoming serial data and display each frame. It also outputs to the console, the size of the frame, the frame rate and the bandwidth being used.

## Features

### Currently working
- [x] Basic grayscale video stream to PC
- [x] Basic python app to decode incoming serial data

### Planned
- [ ] Atleast 30 FPS video
- [ ] Minimal compression artifacts
- [ ] Control of the camera from the PC
- [ ] More advanced COM port detection
- [ ] More informative serial status communication
- [ ] LED status lighting
- [ ] Control of an 8x8 LED matrix from the PC
