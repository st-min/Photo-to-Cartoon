# Photo-to-Cartoon
내가 원하는 영상을 만화(cartoon) 스타일로 변환


##Good Case
원본
![0276_07](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/7d98dbeb-bd13-4fba-a086-61cc8f85b5f7)
만화풍
![0276_07_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/0150fbc1-4b76-4d1a-97cd-3fcac171e6cf)

![0277_07](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/09b471ae-45a6-437f-af0e-d8502bb1cefc)
![0277_07_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/1ac51fb3-beb7-468d-b586-f33e9008d62a)

##Bad Case
![0277_01](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/c4fc042c-8fc7-49a3-8793-869fcefa1498)
![0277_01_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/f61d5861-a550-43f7-91c5-5051b7792443)

![0277_10](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/02874e6c-5fb8-418f-a8eb-6bfe622489c3)
![0277_10_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/652f9037-dab3-406d-ba10-6cbe395b7795)



####영상에 사용한 카메라 및 필름 정보
카메라 : 캐논 QL17 G3
필름 : Kodak Gold 200


### 동작 결과 및 한계
![0277_05](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/b51e96c0-6173-44d1-a0e6-a5dbd5aebd0d)
![0277_05_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/4d7eb5bd-23b9-4110-aef7-7a94c33438ee)

노출이 고른 이미지, 대비가 뚜렷한 이미지에서 괜찮은 결과물을 얻을 수 있음.

그렇지 못한 영역에서 다음과 같은 현상 발생

필름 영상물 특유의 노이즈을 지우는 것에 Blue 기능이 잘 작동한다.


고주파 영역에서 edge detection 어려움으로 인한 만화풍의 변화가 잘되지 않는다.


저조도 환경의 이미지 또는 노출이 부족한 사진의 어두운 영역대에서 edge detection 어려움으로 인한 표현 어려움.


어두운 영역을 밝게 만드는 Shedding Light 기능을 추가하여 edge detection을 하면 만족스러운 결과물을 얻을 수 있을 것 같다.


초점이 맞지 않는 사진 등 Blur한 사진에서 만족스러운 결과물을 얻기 힘들다.
