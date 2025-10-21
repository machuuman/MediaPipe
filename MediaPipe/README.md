# 손 감지 및 얼굴 감지 프로젝트

간단한 소개 문장을 한두 줄로 작성합니다. 이 프로젝트는 손과 얼굴을 감지하는 기능을 제공하며, 제공된 파일들을 사용하여 로컬 환경에서 테스트할 수 있습니다.

![배너 이미지](assets/banner.svg)

## 목차

- [소개](#소개)
- [설치](#설치)
- [사용법](#사용법)
- [예시](#예시)
- [로드맵](#로드맵)
- [기여](#기여)
- [라이선스](#라이선스)

## 소개

이 프로젝트는 손과 얼굴을 감지하는 기능을 구현하며, 웹캠이나 동영상 파일을 통해 실시간 감지를 테스트할 수 있습니다. 이 프로젝트는 `mediapipe` 라이브러리를 활용하여 손과 얼굴을 추적하고, 추가적으로 배경 흐리게 처리하는 기능도 제공합니다. 대상 사용자는 컴퓨터 비전과 AI를 활용한 프로젝트에 관심이 있는 개발자들입니다.

## 설치

필요한 환경과 설치 방법은 아래와 같습니다. 해당 명령어들을 실행하여 필요한 라이브러리들을 설치하세요.

```bash
# 프로젝트를 클론한 후 필요한 라이브러리 설치
git clone https://github.com/yourusername/hand-and-face-detection.git
cd hand-and-face-detection
pip install -r requirements.txt

필수 라이브러리 설치
pip install opencv-python mediapipe yt-dlp

사용법
손 감지 실행

1 hand_detector.py 파일을 열고, 아래 코드를 확인합니다.

cap = cv2.VideoCapture(0)  # 웹캠에서 입력받기
# cap = cv2.VideoCapture("hand.mp4")  # 동영상 파일을 사용할 경우 이 코드를 사용

2 아래 명령어로 손 감지를 실행합니다:
python hand_detector.py
실행 후 ESC 키로 종료할 수 있습니다.

얼굴 감지 실행

face_detector.py 파일을 열고, 필요한 설정을 확인합니다.
cap = cv2.VideoCapture(0)  # 웹캠에서 입력받기
# cap = cv2.VideoCapture("face.mp4")  # 동영상 파일을 사용할 경우 이 코드를 사용
아래 명령어로 얼굴 감지를 실행합니다:
python face_detector.py

YouTube 동영상 링크 입력

YouTube 동영상 링크를 입력받아 처리할 수 있습니다. 이를 위해 yt-dlp 패키지를 사용합니다.

yt-dlp <YouTube 동영상 링크>
다운로드된 동영상을 프로젝트 폴더에 넣고, 코드에서 경로를 설정하여 테스트할 수 있습니다.

예시
기능	설명
손 감지	웹캠 또는 동영상을 통해 손을 감지하는 기능
얼굴 감지	웹캠 또는 동영상을 통해 얼굴을 감지하는 기능
배경 흐리기	배경을 흐리게 처리하여 전경을 강조하는 기능
YouTube 테스트	YouTube 동영상 링크를 입력받아 동영상을 처리하는 기능

