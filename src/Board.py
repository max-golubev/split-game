from BigCell import *


class Board:
    def __init__(self, width, height):
        self.current_player = PLAYER_1
        self.columns = width
        self.rows = height
        self.cells = width * [None]
        for x in range(0, width):
            column = height * [None]
            self.cells[x] = column
            for y in range(0, height):
                column[y] = BigCell(x, y, width, height)

    def get_current_player(self):
        return self.current_player

    def finish_turn(self):
        self.current_player = self.compute_next_player()
        return self.get_current_player()

    def perform_turn(self, cell: BigCell, direction: Direction):
        if cell.get_cell_owner(direction) != NOONE:
            return False
        owner = cell.get_owner()
        if owner != NOONE and owner != self.current_player:
            return False
        cell.set_cell_owner(direction, self.current_player)
        if cell.is_full():
            self.explode(cell)
        return True

    def explode(self, cell: BigCell):
        queue = [cell]
        while len(queue) > 0:
            next = queue.pop(0)
            next.clear()
            for next in self.neighbours(next).items():
                dir, neighbour = next
                origin = dir.get_opposite()
                neighbour.capture(self.current_player, origin)
                if neighbour.is_full():
                    queue.append(neighbour)


    def neighbours(self, cell: BigCell):
        result = {}
        x = cell.get_x()
        y = cell.get_y()
        if cell.has_top():
            result[Direction.TOP] = self.get_cell(x, y - 1)
        if cell.has_right():
            result[Direction.RIGHT] = self.get_cell(x + 1, y)
        if cell.has_bottom():
            result[Direction.BOTTOM] = self.get_cell(x, y + 1)
        if cell.has_left():
            result[Direction.LEFT] = self.get_cell(x - 1, y)
        return result

    def compute_next_player(self):
        current = self.get_current_player()
        if current == PLAYER_1:
            return PLAYER_2
        if current == PLAYER_2:
            return PLAYER_3
        if current == PLAYER_3:
            return PLAYER_4
        if current == PLAYER_4:
            return PLAYER_1
        raise "Unknown player: " + repr(current)

    def get_cell(self, col, row) -> BigCell:
        return self.cells[col][row]

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows
