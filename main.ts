basic.showIcon(IconNames.Heart)
basic.forever(function () {
    servos.P0.setAngle(0)
    basic.pause(1000)
    servos.P0.setAngle(180)
    basic.pause(1000)
})
