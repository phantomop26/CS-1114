"""
Author: [Sahil Kumar Singh]
Assignment / Part: HW2 - Q2 (Harmonic Analysis)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import math
##INPUT
frequency = input("Enter a value for the frequency, w: ")
frequency = float(frequency)

time = input("Enter a value for the duration of the sound wave, T: ")
time = float(time)

##calculation
t=math.sin(frequency*time)
amplitude=(2*t)/frequency
amplitude=round(amplitude,3)
##OUTPUT
print("The amplitude spectrum of this Fourier transform is:", amplitude)

