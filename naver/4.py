# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Point2D  # library with types used in the task      

def solution(A):

    # write your code in Python 3.6
    linear = []
    real_pos = []
    for pos in A:
        real_pos.append(tuple([pos.x, pos.y]))

    for pos in real_pos:
        for pos2 in real_pos:
            for pos3 in real_pos:
                if (pos[0] == pos2[0] and pos[1] == pos2[1]) or (pos[0] == pos3[0] and pos[1] == pos3[1]) or (pos2[0] == pos3[0] and pos2[1] == pos3[1]):
                    continue
                if pos3[0] == pos2[0] == pos[0]:
                    linear_pos = [pos, pos2, pos3]
                    linear_pos.sort()
                    linear.append(tuple(linear_pos))
                elif pos3[1] == pos2[1] == pos[1]:
                    linear_pos = [pos, pos2, pos3]
                    linear_pos.sort()
                    linear.append(tuple(linear_pos))

                elif pos2[1] != pos[1]:
                    standard = (pos2[0] - pos[0]) / (pos2[1] - pos[1])

                    if pos3[1] != pos[1]:
                        gradient = (pos3[0] - pos[0]) / (pos3[1] - pos[1])
                        if gradient == standard:
                            linear_pos = [pos, pos2, pos3]
                            linear_pos.sort()
                            linear.append(tuple(linear_pos))

    linear = set(linear)
    return len(linear)