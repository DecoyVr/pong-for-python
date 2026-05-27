import random

# Stage 
stage.set_background("space")
stage.disable_floor()
stage.disable_all_walls()

# score
left_score = 0
right_score = 0

#Paddles 
left_paddle = codesters.Rectangle(-210, 0, 15, 80, "white")
left_paddle.set_gravity_off()

right_paddle = codesters.Rectangle(210, 0, 15, 80, "white")
right_paddle.set_gravity_off()

# Ball 
ball = codesters.Rectangle(0, 0, 15, 15, "yellow")
ball.set_gravity_off()
ball.set_x_speed(4)
ball.set_y_speed(3)

# Labels 
codesters.Text("PONG", 0, 215, "white")
codesters.Text("W/S = Left Paddle     UP/DOWN = Right Paddle", 0, -225, "gray")

#  Paddle keys 
def w_key():
    y = left_paddle.get_y()
    if y < 185:
        left_paddle.go_to(-210, y + 20)

def s_key():
    y = left_paddle.get_y()
    if y > -185:
        left_paddle.go_to(-210, y - 20)

def up_key():
    y = right_paddle.get_y()
    if y < 185:
        right_paddle.go_to(210, y + 20)

def down_key():
    y = right_paddle.get_y()
    if y > -185:
        right_paddle.go_to(210, y - 20)

stage.event_key("w", w_key)
stage.event_key("s", s_key)
stage.event_key("up", up_key)
stage.event_key("down", down_key)

#  Loop 
def game_loop():
    global left_score, right_score

    bx  = ball.get_x()
    by  = ball.get_y()
    bxs = ball.get_x_speed()
    bys = ball.get_y_speed()

    # Top / bottom wall bounce
    if by >= 220:
        ball.set_y_speed(-abs(bys))
    elif by <= -215:
        ball.set_y_speed(abs(bys))

    # Ball exits right → left player scores
    if bx >= 250:
        left_score += 1
        ball.say("Left: " + str(left_score))
        ball.go_to(0, 0)
        ball.set_x_speed(-4)
        ball.set_y_speed(random.choice([-3, 3]))

    # Ball exits left → right player scores
    elif bx <= -250:
        right_score += 1
        ball.say("Right: " + str(right_score))
        ball.go_to(0, 0)
        ball.set_x_speed(4)
        ball.set_y_speed(random.choice([-3, 3]))

    # Left
    lpy = left_paddle.get_y()
    if bx <= -195 and bx >= -225 and by <= lpy + 45 and by >= lpy - 45 and bxs < 0:
        ball.set_x_speed(abs(bxs) + 0.5)

    # Right
    rpy = right_paddle.get_y()
    if bx >= 195 and bx <= 225 and by <= rpy + 45 and by >= rpy - 45 and bxs > 0:
        ball.set_x_speed(-(abs(bxs) + 0.5))

stage.event_interval(game_loop, 0.05)
