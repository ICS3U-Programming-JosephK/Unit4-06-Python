#!/usr/bin/env python3
# Created by: Joseph Kwon
# Created on: November 23 2022
# This program prints different RGB colour codes
# to the console using nested for loops.


def main():

    # initialize the colors
    red = 0
    green = 0
    blue = 0

    # display opening message
    print("Here are RGB color variations up to 50:")
    print("")

    # determines the different color codes
    # displays results to the console
    for blue in range(0, 51, 1):
        print("\33[34mRGB ({}, {}, {})".format(red, green, blue))
        if blue == 50:
            print("")
            for green in range(1, 51, 1):
                blue = 0
                print("\33[32mRGB ({}, {}, {})".format(red, green, blue))
                if green == 50:
                    print("")
                    for red in range(1, 51, 1):
                        green = 0
                        # pycodestyle marks this line wrong for some reason!
                        print("\33[31mRGB"
                        "({}, {}, {})".format(red, green, blue))


if __name__ == "__main__":
    main()
