from dataclasses import dataclass
from enum import Enum, auto
from abc import abstractmethod
from math import gcd
from typing import Callable, Union


class MJParm(Enum):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class version(MJParm):
    # MJ5_1 = "version 5.1"
    # MJ5_2 = "version 5.2"
    # MJ6 = "version 6"
    MJ6_1 = "version 6.1"
    # NJ5 = "niji 5"
    NJ6 = "niji 6"

    def __call__(self):
        return f"--{self.value}"


class speed(MJParm):
    relax = auto()
    fast = auto()
    turbo = auto()

    def __call__(self):
        return f"--{self.name}"


class quality(MJParm):
    quater = 0.25
    half = 0.5
    whole = 1
    double = 2

    def __call__(self):
        return f"--quality {self.value}"


EnumParm = (version, speed, quality)


class ToggleParm(MJParm):
    video = auto()
    tile = auto()

    def __call__(self):
        return f"--{self.name}"


Number = Union[int, float]


class NumParm(MJParm):
    chaos = 0, 100, int, 0
    repeat = 2, 40, int, 2
    seed = 0, (2 ** 30), int, 0
    stop = 10, 100, int, 100
    stylize = 0, 1000, int, 100
    weird = 0, 3000, int, 0
    sv = 1, 4, int, 4

    def __init__(self, minValue: Number, maxValue: Number, valuetype: type, default: Number):
        assert all(map(lambda x: type(x) is valuetype, (minValue, maxValue, default))), \
            "min and max types must match with valuetype"
        self.min = minValue
        self.max = maxValue
        self.type = valuetype
        self.default = default

    def RefineValue(self, value: Number):
        assert type(value) is self.type, "value type must match with valuetype"
        v = max(self.min, min(self.max, self.type(value)))
        return v

    def __call__(self, value: Number):
        v = self.default if value is None else self.RefineValue(value)
        return f"--{self.name} {v}"


def SplitUniqueSort(s: str):
    words = list(filter(bool, set(s.split(' '))))
    words.sort()
    return ' '.join(words)


def AsIs(s: str):
    return s


def AspectEval(s: str):
    try:
        assert ':' in s, "Aspect ratio must be in the form of 'width:height'"
        # find number of ':' in s
        assert s.count(':') == 1, "Aspect ratio must be in the form of 'width:height'"

        try:
            ratios = tuple(map(int, s.split(':')))
        except ValueError:
            raise ValueError("Aspect ratio must be numeric.")

        w, h = ratios
        assert w <= 14 and h <= 14, f"Larger side ratio must be less than 14. input: {w}:{h}"
        assert w >= 1 and h >= 1, f"Smaller side ratio must be greater than 1. input: {w}:{h}"
        return f"{w}:{h}"
    except Exception as e:
        print(type(e).__name__, ":", e)
        return ""


class StrParm(MJParm):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return SplitUniqueSort, 0

    # no = auto()
    style = AsIs, 0
    aspect = AspectEval, 0

    def __init__(self, evaluator: Callable[[str], str], dummy: int = 0):
        # dummy is for Enum to work properly.
        # python prevent to assign a function to enum value.
        # Therefore, I used dummy to make it tuple.
        self.__evaluator = evaluator

    def __call__(self, value: str):
        if not value:
            print(f"Empty value for {self.name} not allowed.")
            return ""
        toReturn = self.__evaluator(value)
        if toReturn:
            return f"--{self.name} {toReturn}"
        return ""


@dataclass(frozen=True)
class ImageInputTypeValue:
    minValue: int | float
    maxValue: int | float
    defaultValue: int | float
    t: type
    prefix: str = ""


class ImageInputType(MJParm):
    iw = ImageInputTypeValue(0.0, 3.0, 1.0, float)
    sw = ImageInputTypeValue(0, 1000, 100, int, "--sref ")
    cw = ImageInputTypeValue(0, 100, 100, int, "--cref ")

    def __call__(self, reference: str, weight: int):
        return f"--{self.name} {reference} --{self.name[0]}v {min(max(weight, self.__min), self.__max)}"
