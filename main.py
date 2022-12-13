basic.show_icon(IconNames.HEART)

def on_forever():
    robotbit.servo(robotbit.Servos.S1, 0)
    basic.pause(1000)
    robotbit.servo(robotbit.Servos.S1, 180)
    basic.pause(1000)
basic.forever(on_forever)
