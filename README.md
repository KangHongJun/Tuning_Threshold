# Tuning_Threshold
[저번 프로젝트](https://github.com/KangHongJun/Origin-NMS/tree/main/sahi_yolox)에서 개발한 알고리즘이 테스트 애매한 성능을 보였기 때문에 포함도를 기준으로 IOU를 계산하고 NMS를 진행하는 알고리즘(IIOU)을 전달받았다.<br>
IIOU는 삭제되면 안되는 박스까지 삭제하여 match_threshold를 조정했고, 조정한 match_threshold 값을 다른 알고리즘에도 적용시키니 성능이 향상되었다.(F1-score 증가) 아래는 그 진행과정이다.

## 조정 전 match(nms)_threshold=0.5, confidence_threshold=0.4, IIOU_threshold=0.9

<div align="center">
   <p float="left">
      <div align = "center">
       <img src="https://github.com/KangHongJun/Tuning_Threshold/blob/main/threshold_tuning/Nt_IIOU.png", width="70%"><br>
     [ IIOU - F1-score : 0.3333 ]
    </div>
  </p>
  잘 인식하는것처럼 보이지만 초록색으로 칠한부분이 뚜렷하게  탐지 안된 것을 볼 수 있다.<br>
  로그를 통해 IIOU가 아닌 NMS에서 삭제된 것을 파악 했고, match(nms)_threshold 값을 0.7로 올렸다.
  <p float="left">
      <div align = "center">
       <img src="https://github.com/KangHongJun/Tuning_Threshold/blob/main/threshold_tuning/IIOU_NMS.png", width="70%"><br>
     [ IIOU - F1-score : 0.4348
    </div>
  </p>
  threshold을 조정하니 merge되어 사라졌던 detect box도 탐지된 것을 볼 수 있다.<br>
</div>

### F1 score 정리
|BeforeTuning|Score|TP|FP|FN|
|------|-----|---|---|---|
|YOLOX|0.1449|5|0|59|
|NMS|0.3617|17|13|47|
|ONMS|0.3736|17|10|47|
|IIOU|0.4348|20|8|44|

|AfterTuning|Score|TP|FP|FN|
|------|-----|---|---|---|
|YOLOX|0.1449|5|0|59|
|NMS|0.2727|12|12|52|
|ONMS|0.3182|14|10|50|
|IIOU|0.3333|15|11|49|
