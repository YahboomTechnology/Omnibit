from microbit import *
import superbit


display.show(Image.HAPPY)

def lightning():
    superbit.motor_control_dual(superbit.M1, superbit.M4, 255, 255, 0)
    sleep(1000)

    superbit.motor_control_dual(superbit.M1, superbit.M4, 0, 0, 0)
    superbit.motor_control_dual(superbit.M2, superbit.M3, 0, 0, 0)
    superbit.motor_control_dual(superbit.M2, superbit.M3, 255, 255, 0)
    sleep(1000)

    superbit.motor_control_dual(superbit.M1, superbit.M4, 0, 0, 0)
    superbit.motor_control_dual(superbit.M2, superbit.M3, 0, 0, 0)
    superbit.motor_control_dual(superbit.M1, superbit.M4, 255, 255, 0)
    sleep(1000)

    superbit.motor_control_dual(superbit.M1, superbit.M4, 0, 0, 0)
    superbit.motor_control_dual(superbit.M2, superbit.M3, 0, 0, 0)

lightning()
