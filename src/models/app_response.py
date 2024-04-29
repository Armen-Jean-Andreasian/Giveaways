from typing import Hashable, Any


class ResponseModel:
    @staticmethod
    def prototype(**kwargs) -> dict[Hashable, Any]:
        """Dynamically generates a dict and returns it. Accepts only keywords arguments."""

        _result = {}
        given_kwargs = locals()['kwargs']

        for kwarg_key, kwarg_val in given_kwargs.items():
            _result[kwarg_key] = kwarg_val

        return _result
