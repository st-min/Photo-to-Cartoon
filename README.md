# Photo-to-Cartoon
내가 원하는 영상을 만화(cartoon) 스타일로 변환

▪ 목표
– 내가 원하는 영상을 만화(cartoon) 스타일로 변환
▪ 미션
– 필수 기능 (5점)
• 컴퓨터비전(예: Image Processing) 기술을 이용해 주어진 영상을 만화 스타일로 변환하기
– ChatGPT 질의 예) “OpenCV를 이용하여 사진을 만화 스타일로 만드는 코드를 작성해줘.”
– 한계 논의 (15점)
• 자신의 알고리즘으로 만화 같은 느낌이 잘 표현되는 영상 만들기 (5점)
• 자신의 알고리즘으로 만화 같은 느낌이 잘 표현되지 않는 영상 만들기 (5점)
• 자신의 알고리즘의 한계에 대해 작성 (5점)

고주파 영역에서 edge detection 어려움으로 인한 만화풍의 변화가 잘되지 않는다.
저조도 환경의 이미지 또는 노출이 부족한 사진의 어두운 영역대에서 edge detection 어려움으로 인한 표현 어려움.
어두운 영역을 밝게 만드는 Shedding Light 기능을 추가하여 edge detection을 하면 만족스러운 결과물을 얻을 수 있을 것 같다.
초점이 맞지 않는 사진 등 Blur한 사진에서 만족스러운 결과물을 얻기 힘들다.
