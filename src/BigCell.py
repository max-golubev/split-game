NOONE = -1

class BigCell:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.max_x = width - 1
        self.max_y = height - 1

        self.left = NOONE
        self.top = NOONE
        self.bottom = NOONE
        self.right = NOONE

    def get_owner(self):
        if self.left != NOONE:
            return self.left
        if self.right != NOONE:
            return self.right
        if self.top != NOONE:
            return self.top
        if self.bottom != NOONE:
            return self.bottom
        return NOONE


    def has_top(self):
        return self.y != 0

    def has_left(self):
        return self.y != 0

    def has_bottom(self):
        return self.y != self.max_y

    def has_right(self):
        return self.x != self.max_x

