import inspect
from types import FunctionType
from typing import Any, Callable


class ObjectUtils:

    @staticmethod
    def is_obj(obj: Any):
        if isinstance(obj, list) or isinstance(obj, dict):
            return True
        else:
            return str(obj).startswith("{") or str(obj).startswith("[")

    @staticmethod
    def has_arguments(func: Callable) -> int:
        """
        返回函数的参数个数
        """
        signature = inspect.signature(func)
        parameters = signature.parameters
        parameter_names = list(parameters.keys())

        # 排除 self 参数
        if parameter_names and parameter_names[0] == 'self':
            parameter_names = parameter_names[1:]

        return len(parameter_names)

    @staticmethod
    def check_method(func: FunctionType) -> bool:
        """
        检查函数是否已实现
        """
        return func.__code__.co_code != b'd\x01S\x00'
