from enum import Enum

import numpy as np
from output_framework.output_framework import OutputFramework

from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode


class Icon(Enum):
    up = np.full((16, 16, 3), 100)
    down = np.full((16, 16, 3), 200)


if __name__ == "main":
    controller = IMUController(TriggerMode.CHECK_LOOP)
    controller.register_trigger(OutputFramework.setWindow, {'ausgabe': Icon.up}, input.rot_x, 0.1, ThresholdType.HIGHER)
    controller.register_trigger(OutputFramework.setWindow, {'ausgabe': Icon.down}, input.rot_x, -0.1, ThresholdType.LOWER)
