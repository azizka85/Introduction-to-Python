class Bill:
    description: str

    def __init__(self, description: str):
        self.description = description    

class Tail:
    length: str

    def __init__(self, length: str):
        self.length = length

class Duck:
    bill: Bill
    tail: Tail

    def __init__(self, bill: Bill, tail: Tail):
        self.bill = bill
        self.tail = tail

    def about(self) -> str:
        return f'This duck has a {self.bill.description} bill and a {self.tail.length} tail'
