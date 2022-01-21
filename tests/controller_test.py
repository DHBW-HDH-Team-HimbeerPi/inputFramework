import numpy as np
from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode
from output_framework.output_framework import OutputFramework

"""class Icon(Enum):
    up = np.full((16, 16, 3), 100)
    down = np.full((16, 16, 3), 200)
"""

if __name__ == "__main__":
    controller = IMUController(TriggerMode.CHECK_LOOP)
    controller.register_trigger(OutputFramework.setWindow, {'ausgabe': np.full((16, 16, 3), 100)}, controller.rot_x,
                                0.1, ThresholdType.HIGHER)
    controller.register_trigger(OutputFramework.setWindow, {'ausgabe': np.full((16, 16, 3), 200)}, controller.rot_x,
                                -0.1, ThresholdType.LOWER)
