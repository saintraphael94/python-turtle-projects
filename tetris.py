# Tetris Game using Python Turtle Graphics
# Fully functional implementation with all standard features

import turtle
import random
import time

# ─────────────────────────────────────────────
# Configuration Constants
# ─────────────────────────────────────────────
CELL_SIZE = 20
GRID_WIDTH = 10
GRID_HEIGHT = 20
OFFSET_X = -150
OFFSET_Y = 100
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
DROP_INTERVAL = 0.5  # seconds per drop

# Colors
COLORS = [
    None,          # 0 = empty
    '#00FFFF',     # 1 = I - cyan
    '#0000FF',     # 2 = J - blue
    '#FF7F00',     # 3 = L - orange
    '#FFFF00',     # 4 = O - yellow
    '#00FF00',     # 5 = S - green
    '#800080',     # 6 = T - purple
    '#FF0000',     # 7 = Z - red
]

# Tetromino shapes (each rotation state)
# Format: list of (row, col) offsets relative to pivot
SHAPES = {
    'I': [
        [(0, -1), (0, 0), (0, 1), (0, 2)],
        [(-1, 0), (0, 0), (1, 0), (2, 0)],
    ],
    'J': [
        [(0, -1), (0, 0), (0, 1), (1, -1)],
        [(-1, 0), (0, 0), (1, 0), (1, 1)],
        [(0, -1), (0, 0), (0, 1), (-1, 1)],
        [(-1, -1), (-1, 0), (0, 0), (1, 0)],
    ],
    'L': [
        [(0, -1), (0, 0), (0, 1), (1, 1)],
        [(-1, 0), (0, 0), (1, 0), (1, -1)],
        [(0, -1), (0, 0), (0, 1), (-1, -1)],
        [(-1, 1), (-1, 0), (0, 0), (1, 0)],
    ],
    'O': [
        [(0, 0), (0, 1), (1, 0), (1, 1)],
    ],
    'S': [
        [(0, 0), (0, 1), (1, -1), (1, 0)],
        [(-1, 0), (0, 0), (0, 1), (1, 1)],
    ],
    'T': [
        [(0, -1), (0, 0), (0, 1), (1, 0)],
        [(-1, 0), (0, 0), (1, 0), (0, 1)],
        [(0, -1), (0, 0), (0, 1), (-1, 0)],
        [(-1, 0), (0, 0), (1, 0), (0, -1)],
    ],
    'Z': [
        [(0, -1), (0, 0), (1, 0), (1, 1)],
        [(-1, 1), (0, 1), (0, 0), (1, 0)],
    ],
}

PIECE_TYPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']


# ─────────────────────────────────────────────
# Piece Class
# ─────────────────────────────────────────────
class Piece:
    """Represents a single falling tetromino."""

    def __init__(self, shape_type):
        self.type = shape_type
        self.rotation = 0
        self.row = 0
        self.col = GRID_WIDTH // 2 - 1
        self.color_index = PIECE_TYPES.index(shape_type) + 1

    def get_blocks(self):
        """Return list of (row, col) positions for current rotation."""
        shape = SHAPES[self.type][self.rotation]
        return [(self.row + dr, self.col + dc) for dr, dc in shape]

    def rotate(self):
        """Advance rotation index."""
        self.rotation = (self.rotation + 1) % len(SHAPES[self.type])


# ─────────────────────────────────────────────
# Game Board Class
# ─────────────────────────────────────────────
class Board:
    """Manages the grid state and line-clearing logic."""

    def __init__(self):
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

    def is_valid(self, piece):
        """Check if piece's current position is valid (within bounds, no collisions)."""
        for row, col in piece.get_blocks():
            if col < 0 or col >= GRID_WIDTH:
                return False
            if row >= GRID_HEIGHT:
                return False
            if row < 0:
                continue
            if self.grid[row][col] != 0:
                return False
        return True

    def place(self, piece):
        """Lock piece into the grid."""
        for row, col in piece.get_blocks():
            if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
                self.grid[row][col] = piece.color_index

    def clear_lines(self):
        """Remove full lines and return count of cleared lines."""
        cleared = 0
        new_grid = []
        for row in self.grid:
            if all(cell != 0 for cell in row):
                cleared += 1
            else:
                new_grid.append(row)
        # Pad with empty rows at top
        for _ in range(cleared):
            new_grid.insert(0, [0] * GRID_WIDTH)
        self.grid = new_grid
        return cleared


# ─────────────────────────────────────────────
# Renderer Class (Turtle Graphics)
# ─────────────────────────────────────────────
class Renderer:
    """Handles all turtle drawing operations."""

    def __init__(self):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)

        # Preview turtle for next piece
        self.preview = turtle.Turtle()
        self.preview.hideturtle()
        self.preview.speed(0)

        # Score text
        self.score_writer = turtle.Turtle()
        self.score_writer.hideturtle()
        self.score_writer.speed(0)
        self.score_writer.penup()
        self.score_writer.goto(150, 250)

    def draw_square(self, x, y, color_index):
        """Draw a single cell square at pixel position (x, y)."""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.color('black', COLORS[color_index])
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(CELL_SIZE)
            self.t.right(90)
        self.t.end_fill()

    def draw_board(self, board, current_piece):
        """Render the entire board including current piece."""
        self.t.clear()

        # Draw grid lines
        self.t.color('#333333')
        for row in range(GRID_HEIGHT + 1):
            y = OFFSET_Y - row * CELL_SIZE
            self.t.penup()
            self.t.goto(OFFSET_X, y)
            self.t.pendown()
            self.t.forward(GRID_WIDTH * CELL_SIZE)
        for col in range(GRID_WIDTH + 1):
            x = OFFSET_X + col * CELL_SIZE
            self.t.penup()
            self.t.goto(x, OFFSET_Y)
            self.t.pendown()
            self.t.goto(x, OFFSET_Y - GRID_HEIGHT * CELL_SIZE)

        # Draw locked cells
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if board.grid[row][col] != 0:
                    x = OFFSET_X + col * CELL_SIZE
                    y = OFFSET_Y - row * CELL_SIZE - CELL_SIZE
                    self.draw_square(x, y, board.grid[row][col])

        # Draw current piece
        if current_piece:
            for row, col in current_piece.get_blocks():
                if row >= 0:
                    x = OFFSET_X + col * CELL_SIZE
                    y = OFFSET_Y - row * CELL_SIZE - CELL_SIZE
                    self.draw_square(x, y, current_piece.color_index)

    def draw_preview(self, piece):
        """Draw next piece preview in a box on the right."""
        self.preview.clear()
        if piece is None:
            return

        start_x = 200
        start_y = 100

        # Draw box
        self.preview.penup()
        self.preview.goto(start_x, start_y)
        self.preview.pendown()
        self.preview.color('black', '#f0f0f0')
        self.preview.begin_fill()
        for _ in range(2):
            self.preview.forward(5 * CELL_SIZE)
            self.preview.right(90)
            self.preview.forward(5 * CELL_SIZE)
            self.preview.right(90)
        self.preview.end_fill()

        # Draw piece
        shape = SHAPES[piece.type][0]
        for dr, dc in shape:
            x = start_x + (dc + 1) * CELL_SIZE
            y = start_y - (dr + 1) * CELL_SIZE
            self.draw_square_on_preview(x, y, piece.color_index)

    def draw_square_on_preview(self, x, y, color_index):
        """Draw square in preview area."""
        self.preview.penup()
        self.preview.goto(x, y)
        self.preview.pendown()
        self.preview.color('black', COLORS[color_index])
        self.preview.begin_fill()
        for _ in range(4):
            self.preview.forward(CELL_SIZE)
            self.preview.right(90)
        self.preview.end_fill()

    def write_score(self, score, level, lines):
        """Display score, level, and lines."""
        self.score_writer.clear()
        self.score_writer.color('white')
        self.score_writer.goto(150, 250)
        self.score_writer.write(f"SCORE: {score}", font=("Arial", 14, "bold"))
        self.score_writer.goto(150, 220)
        self.score_writer.write(f"LEVEL: {level}", font=("Arial", 14, "bold"))
        self.score_writer.goto(150, 190)
        self.score_writer.write(f"LINES: {lines}", font=("Arial", 14, "bold"))

    def game_over(self, score):
        """Display game over screen."""
        self.t.clear()
        self.t.penup()
        self.t.goto(-80, 50)
        self.t.color('white')
        self.t.write("GAME OVER", font=("Arial", 32, "bold"))
        self.t.goto(-60, 0)
        self.t.write(f"Score: {score}", font=("Arial", 20, "bold"))
        self.t.goto(-80, -40)
        self.t.write("Press R to Restart Game", font=("Arial", 14, "normal"))

    def draw_paused(self):
        """Draw pause overlay."""
        self.t.penup()
        self.t.goto(-60, 50)
        self.t.color('white')
        self.t.write("PAUSED", font=("Arial", 32, "bold"))
        self.t.goto(-50, 10)
        self.t.write("Press P to resume", font=("Arial", 14, "normal"))


# ─────────────────────────────────────────────
# Game Controller Class
# ─────────────────────────────────────────────
class TetrisGame:
    """Main game logic and loop."""

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen.title("Tetris - Turtle Graphics")
        self.screen.bgcolor('#1a1a2e')
        self.screen.tracer(0)
        self.screen.listen()

        self.board = Board()
        self.renderer = Renderer()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over_flag = False
        self.paused = False

        self.current_piece = None
        self.next_piece = None

        self.last_drop_time = time.time()

        self._setup_keybindings()

    def _setup_keybindings(self):
        """Bind keyboard events."""
        self.screen.onkey(self._move_left, 'Left')
        self.screen.onkey(self._move_right, 'Right')
        self.screen.onkey(self._move_down, 'Down')
        self.screen.onkey(self._rotate, 'Up')
        self.screen.onkey(self._hard_drop, 'space')
        self.screen.onkey(self._pause, 'p')
        self.screen.onkey(self._pause, 'P')
        self.screen.onkey(self._restart, 'r')
        self.screen.onkey(self._restart, 'R')

    def _spawn_piece(self):
        """Create a new random piece."""
        piece_type = random.choice(PIECE_TYPES)
        return Piece(piece_type)

    def _move_left(self):
        """Attempt to move piece left."""
        if self.game_over_flag or self.paused:
            return
        self.current_piece.col -= 1
        if not self.board.is_valid(self.current_piece):
            self.current_piece.col += 1

    def _move_right(self):
        """Attempt to move piece right."""
        if self.game_over_flag or self.paused:
            return
        self.current_piece.col += 1
        if not self.board.is_valid(self.current_piece):
            self.current_piece.col -= 1

    def _move_down(self):
        """Attempt soft drop (move down one row)."""
        if self.game_over_flag or self.paused:
            return
        self.current_piece.row += 1
        if not self.board.is_valid(self.current_piece):
            self.current_piece.row -= 1
            self._lock_piece()

    def _rotate(self):
        """Attempt rotation with wall kick adjustments."""
        if self.game_over_flag or self.paused:
            return
        old_rotation = self.current_piece.rotation
        self.current_piece.rotate()

        # Wall kick offsets to try
        kicks = [0, -1, 1, -2, 2]
        for kick in kicks:
            self.current_piece.col += kick
            if self.board.is_valid(self.current_piece):
                return
            self.current_piece.col -= kick

        # Revert rotation if no valid position found
        self.current_piece.rotation = old_rotation

    def _hard_drop(self):
        """Instant drop to lowest valid position."""
        if self.game_over_flag or self.paused:
            return
        while self.board.is_valid(self.current_piece):
            self.current_piece.row += 1
        self.current_piece.row -= 1
        self._lock_piece()

    def _pause(self):
        """Toggle pause state."""
        if self.game_over_flag:
            return
        self.paused = not self.paused
        if self.paused:
            self.last_drop_time = time.time()

    def _lock_piece(self):
        """Lock piece into board, clear lines, spawn new piece."""
        self.board.place(self.current_piece)

        lines = self.board.clear_lines()
        if lines > 0:
            self._update_score(lines)

        self.current_piece = self.next_piece
        self.next_piece = self._spawn_piece()
        self.renderer.draw_preview(self.next_piece)

        # Check game over
        if not self.board.is_valid(self.current_piece):
            self._trigger_game_over()

    def _update_score(self, lines):
        """Update score based on lines cleared."""
        self.score += lines
        self.lines_cleared += lines

        # Level up every 10 lines
        new_level = self.lines_cleared // 10 + 1
        if new_level > self.level:
            self.level = new_level

    def _trigger_game_over(self):
        """Set game over flag."""
        self.game_over_flag = True

    def _restart(self):
        """Reset game state and restart."""
        self.board = Board()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over_flag = False
        self.paused = False
        self.last_drop_time = time.time()
        self.current_piece = self._spawn_piece()
        self.next_piece = self._spawn_piece()
        self.renderer.t.clear()
        self.renderer.draw_preview(self.next_piece)
        self._game_loop()

    def _get_drop_speed(self):
        """Return drop interval based on current level."""
        return max(0.05, DROP_INTERVAL - (self.level - 1) * 0.05)

    def _game_loop(self):
        """Main game loop."""
        if self.game_over_flag:
            self.renderer.game_over(self.score)
            self.screen.update()
            return

        current_time = time.time()
        if not self.paused:
            if current_time - self.last_drop_time >= self._get_drop_speed():
                self.current_piece.row += 1
                if not self.board.is_valid(self.current_piece):
                    self.current_piece.row -= 1
                    self._lock_piece()
                self.last_drop_time = current_time

        if self.game_over_flag:
            self.renderer.game_over(self.score)
        else:
            self.renderer.draw_board(self.board, self.current_piece)
            self.renderer.write_score(self.score, self.level, self.lines_cleared)
            if self.paused:
                self.renderer.draw_paused()
        self.screen.update()

        self.screen.ontimer(self._game_loop, 16)  # ~60 FPS

    def run(self):
        """Start the game."""
        self.current_piece = self._spawn_piece()
        self.next_piece = self._spawn_piece()
        self.renderer.draw_preview(self.next_piece)
        self._game_loop()
        self.screen.mainloop()


# ─────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────
if __name__ == '__main__':
    game = TetrisGame()
    game.run()
