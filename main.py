import cv2
import mediapipe as mp

cap = cv2.VideoCapture('cam1.avi')
fps = cap.get(cv2.CAP_PROP_FPS)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# Threshold untuk deteksi jatuh berdasarkan ketinggian
height_threshold = 0.5
prev_head_height = None
fall_frame_count = 0
total_frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    total_frame_count += 1
    frame = cv2.resize(frame, (980, 740))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    if results.pose_landmarks:
        # Ambil semua koordinat landmark
        h, w, _ = frame.shape
        landmark_coords = []
        for landmark in results.pose_landmarks.landmark:
            x = int(landmark.x * w)
            y = int(landmark.y * h)
            landmark_coords.append((x, y))

        # Hitung bounding box
        min_x = min(landmark_coords, key=lambda x: x[0])[0]
        max_x = max(landmark_coords, key=lambda x: x[0])[0]
        min_y = min(landmark_coords, key=lambda x: x[1])[1]
        max_y = max(landmark_coords, key=lambda x: x[1])[1]

        # Ambil keypoints kepala
        landmarks = results.pose_landmarks.landmark
        nose = landmarks[mp_pose.PoseLandmark.NOSE]
        left_eye = landmarks[mp_pose.PoseLandmark.LEFT_EYE]
        right_eye = landmarks[mp_pose.PoseLandmark.RIGHT_EYE]

        # Hitung centroid kepala
        x_head = int((nose.x + left_eye.x + right_eye.x) / 3 * w)
        y_head = int((nose.y + left_eye.y + right_eye.y) / 3 * h)

        # Hitung rasio ketinggian kepala relatif terhadap tinggi tubuh
        body_height = max_y - min_y
        if body_height > 0:
            head_ratio = (y_head - min_y) / body_height

        height = max_y-min_y
        width = max_x-min_x

        # Gambar elemen visual
        cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)
        cv2.circle(frame, (x_head, y_head), 6, (0, 255, 0), -1)
        cv2.putText(frame, f'Head Ratio: {head_ratio:.2f}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        # Deteksi jatuh berdasarkan head_ratio dan bounding box
        if (head_ratio > height_threshold) and (height-width)<0:
            fall_frame_count += 1
            cv2.putText(frame, "Fall Detected!", (x_head - 20, y_head - 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("Fall Detection by Head Height", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Jumlah seluruh frame         :", total_frame_count)
print("Jumlah frame terdeteksi jatuh:", fall_frame_count)