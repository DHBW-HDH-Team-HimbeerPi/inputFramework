import asyncio
from abc import ABC
from enum import Enum


class TriggerMode(Enum):
    CALL_CHECK = 1
    CHECK_LOOP = 2


class ThresholdType(Enum):
    LOWER = 0
    EQUAL = 1
    HIGHER = 2


class Controller(ABC):
    def __init__(self, trigger_mode: TriggerMode = TriggerMode.CHECK_LOOP):
        self.registered_triggers = []
        self.exit = False

        async def check_loop():
            while True:
                self.check_triggers()

        if trigger_mode is TriggerMode.CHECK_LOOP:
            check_loop()

    def rot_x(self):
        pass

    def rot_y(self):
        pass

    def rot_z(self):
        pass

    def mov_x(self):
        pass

    def mov_y(self):
        pass

    def mov_z(self):
        pass

    def register_trigger(self, function_to_trigger: object, function_kwargs: dict,
                         trigger_function: object, threshold: int, threshold_type: ThresholdType):
        if function_kwargs is None:
            function_kwargs = {}
        trigger_function = {'function_to_trigger': function_to_trigger,
                            'function_kwargs': function_kwargs,
                            'trigger_function': trigger_function,
                            'threshold': threshold,
                            'threshold_type': threshold_type}
        self.registered_triggers.append(trigger_function)

    def check_triggers(self):
        for trigger in self.registered_triggers:
            if (trigger['threshold'] == ThresholdType.LOWER) \
                    and (trigger['trigger_function']() < trigger['threshold']):
                print(f"trigger {trigger['trigger_function']}")
                trigger['function_to_trigger'](**trigger['function_kwargs'])
            if (trigger['threshold'] == ThresholdType.EQUAL) \
                    and (trigger['trigger_function']() == trigger['threshold']):
                trigger['function_to_trigger'](**trigger['function_kwargs'])
            if (trigger['threshold'] == ThresholdType.HIGHER) \
                    and (trigger['trigger_function']() > trigger['threshold']):
                trigger['function_to_trigger'](**trigger['function_kwargs'])
