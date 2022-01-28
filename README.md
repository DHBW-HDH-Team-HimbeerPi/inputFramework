# Input Framework
### needed imports
```python
from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode
```
### initialyze controller
```python
controller = IMUController()
```

You need to call ```controller.check_triggers()``` in your main loop.

### registering triggers
your triggers could look something like this
```python 
rotationThreshold = 0.35
controller.register_trigger(moveSnake, {'direction' : 1}, controller.mov_x, rotationTreshold, ThresholdType.HIGHER)
controller.register_trigger(moveSnake, {'direction' : 2}, controller.mov_x, -rotationTreshold, ThresholdType.LOWER)
controller.register_trigger(moveSnake, {'direction' : 3}, controller.mov_y, -rotationTreshold, ThresholdType.LOWER)
controller.register_trigger(moveSnake, {'direction' : 4}, controller.mov_y, rotationTreshold, ThresholdType.HIGHER)
```
The following threshold types modes exist:
- ```ThresholdType.LOWER```
- ```ThresholdType.EQUALS```
- ```ThresholdType.HIGHER```


The function ```moveSnake``` will be called with the argument ```1``` if the acceleration in x direction is more higher than 0.35 m/s²
