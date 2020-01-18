
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
sense.show_message("HALLO RUIMTEVAARDERS", text_colour=(225,0,0),back_colour=(245,255,60),scroll_speed=0.02)
sense.set_pixel(3,4,(255,0,0))
sense.set_pixel(3,3,(255,0,0))
sense.set_pixel(4,3,(255,0,0))   

temp = sense.get_temperature()
pressure = sense.get_pressure()
humidity = sense.get_humidity()

sense.show_message("T:", text_colour=(225,0,0),
                   back_colour=(0,0,0), scroll_speed=0.12
                  )
sense.show_message(str(round(temp,1)), text_colour=(225,0,0), 
                   back_colour=(0,0,0), scroll_speed=0.1)
                   
sense.show_message("P:", text_colour=(225,0,0),
                   back_colour=(0,0,0), scroll_speed=0.12)
sense.show_message(str(round(pressure,0)), text_colour=(225,0,0),
                   back_colour=(0,0,0), scroll_speed=0.1)
                   
sense.show_message("H:", text_colour=(225,0,0),
                   back_colour=(0,0,0),scroll_speed=0.12)
sense.show_message(str(round(humidity,0)), text_colour=(225,0,0),
                   back_colour=(0,0,0), scroll_speed=0.1)
