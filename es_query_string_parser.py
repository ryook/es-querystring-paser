from exceptions import ValidationError
from parser import parser


class EsQueryStringParser:

    def __init__(self) -> None:
        pass

    def validate(self, string: str) -> bool:
        try:
            parser(string)
        except Exception as e:
            raise ValidationError(e)
        return True
