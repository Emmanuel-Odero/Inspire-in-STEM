from machine import Pin, Timer

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
LED_state1 = True
LED_state2 = True
tim =Timer()

def tick(timer):
    global led, LED_state1, LED_state2
    LED_state1 = not LED_state1
    LED_state2 = not LED_state2
    led1.value(LED_state1)
    led2.value(LED_state2)
    
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
    