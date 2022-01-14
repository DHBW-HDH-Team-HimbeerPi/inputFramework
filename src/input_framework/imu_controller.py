from src.input_framework.interface import Controller, TriggerMode, ThresholdType
from src.input_framework.sensor_wrapper import SparkfunIcm20948Adapter


class IMUController(Controller):
    def __init__(self, trigger_mode: TriggerMode = TriggerMode.check_loop):
        super().__init__(trigger_mode)
        self.imu = SparkfunIcm20948Adapter()

    @property
    def rot_x(self):
        return self.imu.scaled_angular_acceleration[0]

    @property
    def rot_y(self):
        return self.imu.scaled_angular_acceleration[1]

    @property
    def rot_z(self):
        return self.imu.scaled_angular_acceleration[2]

    @property
    def mov_x(self):
        return self.imu.scaled_acceleration[0]

    @property
    def mov_y(self):
        return self.imu.scaled_acceleration[0]

    @property
    def mov_z(self):
        return self.imu.scaled_acceleration[0]

    def check_triggers(self):
        for trigger in self.registered_triggers:
            if (trigger['threshold'] == ThresholdType.lower) and (trigger['trigger_function']() < trigger['threshold']):
                trigger['function_to_trigger'](**trigger['function_kwargs'])
            if (trigger['threshold'] == ThresholdType.equal) and (trigger['trigger_function']() == trigger['threshold']):
                trigger['function_to_trigger'](**trigger['function_kwargs'])
            if (trigger['threshold'] == ThresholdType.higher) and (trigger['trigger_function']() > trigger['threshold']):
                trigger['function_to_trigger'](**trigger['function_kwargs'])
