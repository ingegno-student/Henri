from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(0)
sense.show_message("HALLO RUIMTEVAARDERS", text_colour=(225,0,0),back_colour=(245,255,60),scroll_speed=0.12)
sense.set_pixel(3,4,(255,0,0))
sense.set_pixel(3,3,(255,0,0))
sense.set_pixel(4,3,(255,0,0))
sense.set_pixel(4,4,(255,0,0))
