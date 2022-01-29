class Production:
    def __init__(self, left_side, right_side, attributes = []) -> None:
        self.left_side = left_side
        self.right_side = right_side
        self.attributes = attributes