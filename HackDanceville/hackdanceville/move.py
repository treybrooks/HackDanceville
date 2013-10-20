import curses

from hackdanceville.queue import DancefloorLoop

def movement_wrapper(func):
    def wrapper(inst, *args, **kwargs):
        print inst.player1Data
        """inst.data[inst.y * 8 + inst.x][inst.color_i] = 0
        func(inst, *args, **kwargs)
        inst.data[inst.y * 8 + inst.x][inst.color_i] = 255"""
        # check to see if player is on top of bomb
        pass
    return wrapper


class Move(object):

    def __init__(self):
        self.init_data()
        """
        Key mapping we care about, comes from jQuery
        16 = shift = player 1 bomb
        37 = left arrow = player 1 left
        38 = up arrow = player 1 up
        39 = right arrow = player 1 right
        40 = down arrow = player 1 down
        81 = q = quit
        68 = d = player 2 right
        65 = a = player 2 left
        70 = f = player 2 down
        83 = s = player 2 up
        71 = g = player 2 bomb
        """
        """self.keymap = {
            16: self.player1_drop_bomb,
            38: self.player1_move_up,
            40: self.player1_move_down,
            37: self.player1_move_left,
            39: self.player1_move_right,
            71: self.player2_drop_bomb,
            83: self.player2_move_up,
            70: self.player2_move_down,
            65: self.player2_move_left,
            68: self.player2_move_right,
            113: self.quit
        }"""
        self.color_i = 1
        self.loop = None
        self.go = False

    def init_data(self):
        #player1 = Player([0, )
        pass

    """def player1_drop_bomb(self):
        self.player1Bomb.setBomb(self.player1X, self.player1Y)

    @movement_wrapper
    def player1_move_left(self):
        self.player1X = (self.player1X - 1) % 8

    @movement_wrapper
    def player1_move_right(self):
        self.player1X = (self.player1X + 1) % 8

    @movement_wrapper
    def player1_move_up(self):
        self.player1Y = (self.player1Y - 1) % 8

    @movement_wrapper
    def player1_move_down(self):
        self.player1Y = (self.player1Y + 1) % 8

    def player2_drop_bomb(self):
        self.player2Bomb.setBomb(self.player2X, self.player2Y)

    @movement_wrapper
    def player2_move_left(self):
        self.player2X = (self.player2X - 1) % 8

    @movement_wrapper
    def player2_move_right(self):
        self.player2X = (self.player2X + 1) % 8

    @movement_wrapper
    def player2_move_up(self):
        self.player2Y = (self.player2Y - 1) % 8

    @movement_wrapper
    def player2_move_down(self):
        self.player2Y = (self.player2Y + 1) % 8"""

    def initialize_loop(self):
        if not self.loop or not self.loop.is_alive():
            self.loop = DancefloorLoop(data=self.player1Data)
            self.loop.start()
            self.go = True

    def quit(self):
        self.player1Data = None
        self.player2Data = None
        self.go = False

    def put(self, key):
        print 'putting ' + str(key)
        if key in self.keymap:
            func = self.keymap[key]
            func()
            print 'ran ' + str(func)
        self.loop.queue.put(self.player1Data)

    def curses_loop(self):
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(1)

        stdscr.addstr(0, 10, "Hit 'q' to quit")
        stdscr.refresh()

        self.initialize_loop()

        while self.go:
            key = stdscr.getch()
            stdscr.addch(20, 25, key)
            stdscr.refresh()
            self.put(key)

        curses.endwin()

class Bomb(object):

    def __init__(self, player):
        self.init_bomb()
        self.player

    def init_bomb(self, color):
        self.x = 0
        self.y = 0
        self.color = color
        self.blinkCount = 0
        self.bombSet = False
        self.exploded = False

    def set_bomb(self, playerPosX, playerPosY):
        if self.bombSet == False:
            print 'bomb set'
            self.x = playerPosX
            self.y = playerPosY
            self.bombSet = True
            self.exploded = False

    def return_data(self):
        if self.bombSet == True:
            self.blinkCount + 1
            if self.blinkCount > 5:
                self.exploded = True
                self.bombSet = False
                self.blinkCount = 0
                player.removeBomb()
        else:
            self.exploded = False
        return self

class Player(object):

    def __init__(self, color):
        self.x = 0
        self.y = 0
        self.color = color
        self.bombs = []

    def move_left(self):
        self.x = (self.x - 1) % 8

    def move_right(self):
        self.x = (self.x + 1) % 8

    def move_up(self):
        self.y = (self.y - 1) % 8

    def move_down(self):
        self.y = (self.y + 1) % 8

    def setBomb(self):
        if self.bombs.count < 4:
            self.bombs.append(Bomb(self))

    def removeBomb(self):
        del self.bombs[0]

    def returnData(self):
        returnObj = {}
        returnObj['x'] = self.x
        returnObj['y'] = self.y
        returnObj['color'] = self.color
        returnObj['bombCount'] = self.bomb.count
        returnObj['bombs'] = []
        for el in self.bombs:
            thisBomb = el.returnData()
            returnObj['bombs'].append(thisBomb)

if __name__ == "__main__":
    m = Move()
    m.curses_loop()
