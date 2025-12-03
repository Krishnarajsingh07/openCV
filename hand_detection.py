import mediapipe as mp
import cv2

# Hand tracking modules
mp_draw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles
mp_hand = mp.solutions.hands

cap = cv2.VideoCapture(0)

p = mp_hand.Hands(
    model_complexity=0,
    max_num_hands=2,
    min_detection_confidence=0.5
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Convert BGR → RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process
    result = p.process(rgb)

    # Convert back RGB → BGR for OpenCV
    frame = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    # Draw landmarks
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hand.HAND_CONNECTIONS,
                mp_draw_styles.get_default_hand_landmarks_style(),
                mp_draw_styles.get_default_hand_connections_style()
            )

    cv2.imshow('frame', frame)

    if cv2.waitKey(25) & 0xFF == ord('p'):
        break

cap.release()
cv2.destroyAllWindows()
