#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp

# =========================================
# 🧩 Mediapipe 초기화
# =========================================
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# 얼굴 감지 모델 초기화
face_detection = mp_face_detection.FaceDetection(
    min_detection_confidence=0.5  # 얼굴 감지 신뢰도
)

# =========================================
# 📸 카메라 연결
# =========================================
# cap = cv2.VideoCapture(0)            # 기본 카메라 사용시
cap = cv2.VideoCapture("face.mp4")   # 동영상 파일 사용 시

print("📷 카메라 스트림 시작 — ESC를 눌러 종료합니다.")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("⚠️ 프레임을 읽지 못했습니다. 카메라 연결을 확인하세요.")
        break

    # 좌우 반전 (셀카 뷰)
    image = cv2.flip(image, 1)

    # BGR → RGB 변환
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 얼굴 감지 수행
    result = face_detection.process(image_rgb)

    # 얼굴 위치 표시
    if result.detections:
        for detection in result.detections:
            # 얼굴 감지 결과에서 bounding box 정보 가져오기
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                         int(bboxC.width * iw), int(bboxC.height * ih)

            # 얼굴 주위에 사각형을 그립니다
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 얼굴 감지 결과에 대한 신뢰도 표시
            cv2.putText(image, f'{int(detection.score[0] * 100)}%', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 🖐️ 손 랜드마크 감지 (선택 사항, 필요 없으면 제거 가능)
    # 손 감지 코드 추가 시 위에서 작성한 Hand 관련 코드 복사 후 붙여넣기 가능

    # 화면 표시
    cv2.imshow('👤 MediaPipe Face Detection', image)

    # ESC 키로 종료
    if cv2.waitKey(5) & 0xFF == 27:
        print("👋 종료합니다.")
        break

# =========================================
# 🔚 종료 처리
# =========================================
cap.release()
cv2.destroyAllWindows()
