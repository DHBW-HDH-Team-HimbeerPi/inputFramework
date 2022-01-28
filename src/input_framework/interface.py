import asyncio
from abc import ABC
from enum import Enum


class TriggerMode(Enum):
    """deprecated"""
    CALL_CHECK = 0
    CHECK_LOOP = 1


class ThresholdType(Enum):
    LOWER = 0
    EQUAL = 1
    HIGHER = 2


class Controller(ABC):
    def __init__(self, legacy_trigger_mode=None):
        # calling this Function with a trigger_mode is deprecated
        self.registered_triggers = []

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
            print(f"trigger acc {trigger['trigger_function']()}")
            if (trigger['threshold_type'] == ThresholdType.LOWER) \
                    and (trigger['trigger_function']() < trigger['threshold']):
                print("trigger lower")
                trigger['function_to_trigger'](**trigger['function_kwargs'])

            if (trigger['threshold_type'] == ThresholdType.EQUAL) \
                    and (trigger['trigger_function']() == trigger['threshold']):
                print("trigger equal")
                trigger['function_to_trigger'](**trigger['function_kwargs'])

            if (trigger['threshold_type'] == ThresholdType.HIGHER) \
                    and (trigger['trigger_function']() > trigger['threshold']):
                print("trigger higher")
                trigger['function_to_trigger'](**trigger['function_kwargs'])
