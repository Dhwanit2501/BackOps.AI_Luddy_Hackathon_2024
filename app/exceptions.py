class KeyAlreadyExist(Exception):
    def __init__(self, key: str) -> None:
        self.key = key

    def __str__(self) -> str:
        return f"Insert Operation Failed! The key: {self.key} is already exist."
    
class KeyNotFound(Exception):
    def __init__(self, key: str, op: str) -> None:
        self.key = key
        self.op = op

    def __str__(self) -> str:
        return f"{self.op} Operation Failed! The key: {self.key} is not exist."
    
class ValueIsEmpty(Exception):
    def __init__(self, key: str) -> None:
        self.key = key

    def __str__(self) -> str:
        return f"Insert Operation Failed! The value of key: {self.key} is not provided"