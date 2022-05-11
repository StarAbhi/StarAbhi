def water_temperature_for_coffee(temp):
    if temp < 195:
        print('Too cold.')
    elif(temp >= 195) and (temp <=205):
        print('Perfect temperature.')
    elif (temp > 205):
        print('Too hot.')

water_temperature_for_coffee(205)
water_temperature_for_coffee(190)
