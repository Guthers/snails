from .abstract_model import AbstractModel


class ExceptionModel(AbstractModel):
    def __init__(self, message: str):
        self.message = message
