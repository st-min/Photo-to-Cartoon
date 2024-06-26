# 내가 원하는 영상을 만화(cartoon) 스타일로 변환

OpenCV를 이용하여 사진을 만화 스타일로 만드는 코드.
경로를 설정해 원하는 위치에 이미지를 읽고 변환 후 저장할 수 있습니다.

## Good Case

원본 ![0276_07](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/7d98dbeb-bd13-4fba-a086-61cc8f85b5f7)
만화 ![0276_07_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/0150fbc1-4b76-4d1a-97cd-3fcac171e6cf)


원본 ![0277_07](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/09b471ae-45a6-437f-af0e-d8502bb1cefc)
만화 ![0277_07_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/1ac51fb3-beb7-468d-b586-f33e9008d62a)


## Bad Case
원본 ![0277_03](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/e30348cc-ef66-47ac-a91e-1ec775f71bde)
만화 ![0277_03_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/4416c915-8753-4534-89df-eb84f67d378b)

원본 ![0276_13](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/a7bbc10c-45f5-4885-957d-4bf1bc5fbac2)
만화 ![0276_13_cartoon](https://github.com/st-min/Photo-to-Cartoon/assets/70586865/a4e40fba-4276-44ae-a83e-20f16a8f4f63)



---
#### 영상에 사용한 카메라 및 필름 정보
카메라 : 캐논 QL17 G3


필름 : Kodak Gold 200

---
### 동작 결과 및 한계

<img width="1170" alt="Screenshot 2024-03-25 at 5 45 46 PM" src="https://github.com/st-min/Photo-to-Cartoon/assets/70586865/760cad7f-84c6-415b-9136-7bde1a0d54b5">

<img width="1170" alt="Screenshot 2024-03-25 at 5 45 40 PM" src="https://github.com/st-min/Photo-to-Cartoon/assets/70586865/71f433d1-6f56-41ec-af59-e774a72054b1">

필름 영상물 특유의 노이즈을 지우는 것에 Blue 기능이 잘 작동한다.

노출이 고른 이미지, 대비가 뚜렷한 이미지에서 괜찮은 결과물을 얻을 수 있다.

저조도 환경 또는 노출이 부족한 사진의 어두운 영역대에서 edge detection 어려움으로 인한 만화풍의 변화가 미비함.

초점이 맞지 않는 사진 등 Blur한 사진에서 만족스러운 결과물을 얻기 힘들다.

어두운 영역을 밝게 만드는 Shedding Light 기능을 추가하여 edge detection을 하면 만족스러운 결과물을 얻을 수 있을 것 같다.
