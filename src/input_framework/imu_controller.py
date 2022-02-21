"""module contains controller for sparkfun imu"""
import atexit

from input_framework.interface import Controller, TriggerMode
from input_framework.sensor_wrapper import SparkfunIcm20948Adapter


class IMUController(Controller):
    def __init__(self, legacy_trigger_mode: TriggerMode = TriggerMode.CHECK_LOOP):
        super().__init__(legacy_trigger_mode)
        self.imu = SparkfunIcm20948Adapter()
        atexit.register(exit)

    def exit(self):
        super().exit = True

    def rot_x(self):
        return self.imu.scaled_angular_acceleration[0]

    def rot_y(self):
        return self.imu.scaled_angular_acceleration[1]

    def rot_z(self):
        return self.imu.scaled_angular_acceleration[2]

    def mov_x(self):
        return self.imu.scaled_acceleration[0]

    def mov_y(self):
        return self.imu.scaled_acceleration[1]

    def mov_z(self):
        return self.imu.scaled_acceleration[2]
