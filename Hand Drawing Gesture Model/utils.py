import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Global state
canvas = None
prev_x, prev_y = None, None
paused = False
color_index = 0
colors = [(0, 128, 128)]
draw_color = colors[color_index]
erase_color = (0, 0, 0)


def fingers_up(hand_landmarks):
    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Fingers
    for tip_id in [8, 12, 16, 20]:
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers


def process_frame(frame):
    global canvas, prev_x, prev_y, draw_color, paused, color_index

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm = handLms.landmark
            x, y = int(lm[8].x * w), int(lm[8].y * h)

            fingers = fingers_up(handLms)
            total_up = sum(fingers)

            if fingers == [0, 1, 0, 0, 0]:
                if not paused and prev_x is not None:
                    cv2.line(canvas, (prev_x, prev_y), (x, y), draw_color, 5)
                prev_x, prev_y = x, y

            elif fingers == [0, 1, 1, 0, 0]:
                if not paused and prev_x is not None:
                    cv2.line(canvas, (prev_x, prev_y), (x, y), erase_color, 20)
                prev_x, prev_y = x, y

            elif total_up == 5:
                color_index = (color_index + 1) % len(colors)
                draw_color = colors[color_index]
                paused = False
                prev_x, prev_y = None, None

            elif total_up == 0:
                paused = True
                prev_x, prev_y = None, None

            elif fingers == [1, 0, 0, 0, 0]:
                canvas = np.zeros_like(frame)
                prev_x, prev_y = None, None

            elif fingers == [0, 1, 0, 0, 0] and paused:
                paused = False
                prev_x, prev_y = None, None

            else:
                prev_x, prev_y = None, None

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    else:
        prev_x, prev_y = None, None

    combined = cv2.addWeighted(frame, 0.7, canvas, 0.3, 0)
    return combined
