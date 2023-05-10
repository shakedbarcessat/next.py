class Pixles:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = int((self._red + self._blue + self._green) / 3)
        self._red = avg
        self._blue = avg
        self._green = avg

    def print_pixel_info(self):
        print("X: " + str(self._x) + ", Y: " + str(self._y) +
              ", Color: " + str(tuple([self._red, self._green, self._blue])), end=" ")
        if self._red == 0 and self._blue == 0 and self._green > 50:
            print("Green")
        elif self._red == 0 and self._green == 0 and self._blue > 50:
            print("Blue")
        elif self._green == 0 and self._blue == 0 and self._red > 50:
            print("Red")


def main():
    p = Pixles(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()
