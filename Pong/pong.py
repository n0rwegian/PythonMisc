'''
The function ball_move args*: w (field width), h (field_height), x_ball (x of the ball before the move),
    y_ball (y of the ball before the move), y_paddle_new_{1?2} (y of the paddle AFTER the move) <- from the
    function moving paddles, x_speed_ball, y_speed_ball
Paddle_1 is supposed to always have x == 1
Paddle_2 is supposed to always have x == h
y_paddle_new_{1?2} corresponds to the top of the paddle, i.e. the paddle_1 placed in the left topmost corner would have
    the y_paddle_1 == 0 the end being y == 2

Collision logic:
    x_ball_speed_new = -x_ball_speed

    As we have the paddle height == 3 then if the y_ball_new ==:
        (top part of the paddle) y_paddle{1?2}_new: y_ball_speed -= 1
        (middle part of the paddle) y_paddle{1?2}_new - 1: y_ball_speed += 0
        (low part of the paddle) y_paddle{1?2}_new: y_ball_speed += 1
'''
import time

def goal(player):
    pass


def ball_move(w, h, x_ball, y_ball, y_paddle_1_new,  y_paddle_2_new, x_speed_ball = 1, y_speed_ball = 1):

    p_h = 3

    # input check
    if x_ball < 0 or x_ball > w:
        print(f'Error: x_ball has incorrect value: {x_ball}')
        return 1
    if y_ball < 0 or y_ball > h:
        print(f'Error: y_ball has incorrect value: {y_ball}')
        return 1
    if y_paddle_1_new < 0 or y_paddle_1_new > h - p_h:
        print(f'Error: y_paddle_1 has incorrect value: {y_paddle_1_new}')
        return 1
    if y_paddle_2_new < 0 or y_paddle_2_new > h - p_h:
        print(f'Error: y_paddle_2 has incorrect value: {y_paddle_2_new}')
        return 1

    # new coordinates if no rebounce and no goal
    x_ball_new = x_ball + x_speed_ball
    y_ball_new = y_ball + y_speed_ball

    # cases of y rebounce from the top or the bottom
    if y_ball_new < 0:
        print(f'Rebounce from the top')
        y_ball_new = -y_ball_new
        y_speed_ball *= -1
        x_ball_new += x_speed_ball
    elif y_ball_new > h:
        print(f'Rebounce from the bottom')
        y_ball_new = h + h - y_ball_new
        y_speed_ball *= -1
        x_ball_new += x_speed_ball

    # cases of goal or possible rebounce
    if x_ball_new <= 0 or x_ball_new >= w:
        print('Goal or rebounce:')
        if x_ball_new < 0:
            print('Goal player 2')
            goal(2)
            return 0
        elif x_ball_new == 0:
            if y_paddle_1_new <= y_ball_new <= y_paddle_1_new + p_h - 1:
                print(f'Rebounce from paddle_1', end=' ')
                x_ball_new = x_ball
                x_speed_ball *= -1
                if y_ball_new == y_paddle_1_new:
                    print(f'top')
                    y_speed_ball -= 1
                elif y_ball_new == y_paddle_1_new + p_h - 1:
                    print(f'bottom')
                    y_speed_ball += 1
                else:
                    print(f'middle')
                y_ball_new += y_speed_ball
        elif x_ball_new > w:
            print(f'goal player 1')
            goal(1)
            return 0
        elif x_ball_new == w:
            if y_paddle_2_new <= y_ball_new <= y_paddle_2_new + p_h - 1:
                print(f'Rebounce from paddle_2', end=' ')
                x_ball_new = x_ball
                x_speed_ball *= -1
                if y_ball_new == y_paddle_2_new:
                    print(f'top')
                    y_speed_ball -= 1
                elif y_ball_new == y_paddle_2_new - p_h + 1:
                    print(f'bottom')
                    y_speed_ball += 1
                else:
                    print(f'middle')
            y_ball_new += y_speed_ball

    # cases of y rebounce from the top or the bottom
    if y_ball_new < 0:
        print(f'Rebounce from the top')
        y_ball_new = -y_ball_new
        y_speed_ball *= -1
        x_ball_new += x_speed_ball
    elif y_ball_new > h:
        print(f'Rebounce from the bottom')
        y_ball_new = h + h - y_ball_new
        y_speed_ball *= -1
        x_ball_new += x_speed_ball

    # output check
    if x_ball_new < 0 or x_ball_new > w:
        print(f'Error: x_ball_new has incorrect value: {x_ball_new}')
        return 1
    if y_ball_new < 0 or y_ball_new > h:
        print(f'Error: y_ball has incorrect value: {y_ball_new}')
        return 1
    if x_speed_ball == 0:
        print(f'Error: x_speed_ball is equal to: {x_speed_ball}')
        return 1

    return x_ball_new, y_ball_new, x_speed_ball, y_speed_ball


width = 80
height = 25

x, y, yp1, yp2, xs, ys = 40, 12, 10, 10, -1, 0
x, y, yp1, yp2, xs, ys = 1, 5, 0, 0, -1, -4
while True:
    print(f'x_ball = {x}, y_ball = {y}, y_paddle_1 = {yp1}, y_paddle_2 = {yp2}, x_speed_ball = {xs}, y_speed_ball = {ys}')
    x, y, xs, ys = ball_move(width, height, x, y, yp1, yp2, xs, ys)
    time.sleep(0.01)















'''
== Quest received. Develop an src/pong.c program for a two-player game, similar to Pong. To display the graphics, only use ASCII characters (with output to the terminal). You need to implement the step-by-step version using only the material of the course studied so far and the standard library.

Keys:
A/Z and K/M - to move the rackets;

Space Bar - to skip an action at a certain step of the game in step-by-step mode.

Graphics
The field is a 80 x 25-symbol rectangle.

Racket size is 3 symbols;

Ball size is 1 symbol.

UI/UX
When one of the players scores 21 points, congratulations to the winner are displayed on the screen and the game ends.==
'''





















