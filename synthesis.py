import pyo

s = pyo.Server().boot()
s.setInputDevice(2)
a = SineLoop(freq=300, feedback=.1, mul=.3)
lf1 = Sine(freq=.04, mul=10)
lf2 = Sine(freq=.05, mul=10)
b = FreqShift(a, shift=lf1, mul=.5).out()
c = FreqShift(a, shift=lf2, mul=.5).out(1)