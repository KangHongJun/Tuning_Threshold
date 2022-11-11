# Tuning_Threshold
[저번 프로젝트](https://github.com/KangHongJun/Origin-NMS/tree/main/sahi_yolox)에서 개발한 알고리즘이 다른 영상에서 애매한 성능을 보였기 때문에 포함도를 기준으로 IOU를 계산하는 알고리즘(IIOU)을 전달받았고, IIOU는 삭제되면 안되는 박스까지 삭제하여 match_threshold를 조정했고, 조정한 match_threshold 값을 다른 알고리즘에도 적용시키니 성능이 향상되었다.(F1-score 증가) 아래는 그 진행과정이다.

## 조정 전 match(nms)_threshold=0.5, confidence_threshold=0.4

<div align="center">
     <p float="left">
    <div align = "center">
       <img src="https://github.com/KangHongJun/Tuning_Threshold/blob/main/threshold_tuning/N_IIOU.png", width="70%"><br>
     [ IIOU - F1-score : 0.3333 ]
    </div>
  </p>
  기존 NMS와
</div>
