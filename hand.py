import cv2
import mediapipe as mp

# Initialize MediaPipe Hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Capture video
cap = cv2.VideoCapture(0)

# Create an empty list to store the finger tip path
finger_path = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        # Get the coordinates of the pinky finger tip
        tip_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * frame.shape[1])
        tip_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * frame.shape[0])

        # Add the pinky finger tip coordinates to the path list
        finger_path.append((tip_x, tip_y))

        # Draw circles at the pinky finger tip position
        cv2.circle(frame, (tip_x, tip_y), 5, (0, 0, 255), -1)

        # Draw a line connecting the points in the pinky finger path
        for i in range(1, len(finger_path)):
            cv2.line(frame, finger_path[i - 1], finger_path[i], (0, 0, 255), 2)

        # Check for the 'j' shape pattern
        if len(finger_path) > 2:
            last_three_points = finger_path[-3:]
            x1, y1 = last_three_points[0]
            x2, y2 = last_three_points[1]
            x3, y3 = last_three_points[2]

            # Check if the path goes straight down and curves like 'j'
            if x2 == x3 and x2 == x1 and y3 > y2 and y2 > y1:
                # Change the color of the letter to green
                cv2.putText(frame, 'Letter: j', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    else:
        # Clear the path when the finger goes off-screen
        finger_path = []

    cv2.imshow('Finger Tip Path', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
