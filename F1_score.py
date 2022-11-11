def F1_score(Pred):
    #GT
    import xml.etree.ElementTree as ET
    GT_path = "path/label.xml"
    GT_tree = ET.parse(GT_path)
    root = GT_tree.getroot()

    X1 = []
    Y1 = []
    X2 = []
    Y2 = []

    for box in root.iter('bndbox'):
        X1.append(int(box[0].text))
        Y1.append(int(box[1].text))
        X2.append(int(box[2].text))
        Y2.append(int(box[3].text))

    X1= torch.tensor(X1)
    Y1 = torch.tensor(Y1)
    X2 = torch.tensor(X2)
    Y2 = torch.tensor(Y2)

    areas = (X2-X1)*(Y2-Y1)

    true_count = 0
    #Pred GT IOU
    for Selected_object_data in Pred:
        Box = Selected_object_data.bbox

        Pred_X1 = torch.tensor(Box.minx)
        Pred_Y1 = torch.tensor(Box.miny)
        Pred_X2 = torch.tensor(Box.maxx)
        Pred_Y2 = torch.tensor(Box.maxy)

        XX1 = torch.max(X1,Pred_X1)
        YY1 = torch.max(Y1,Pred_Y1)
        XX2 = torch.min(X2,Pred_X2)
        YY2 = torch.min(Y2,Pred_Y2)

        w = XX2 - XX1
        h = YY2 - YY1

        w = torch.clamp(w,min=0.0)
        h = torch.clamp(h, min=0.0)

        inter = w*h

        #IOU
        Pred_area = (Pred_X2-Pred_X1)*(Pred_Y2-Pred_Y1)
        union = (areas - inter) + Pred_area
        match_metric_value = inter/union

        mask = match_metric_value>=0.8
        if sum(mask)==1:
            true_count+=1

    # TureP : IOU비교하여 0.8<=만족하는 데이터
    # FalseP : IOU비교하여 0.8<=만족하지 않는 데이터
    # FalseN : 놓친 데이터
    TP = true_count
    FP = len(Pred) - true_count
    FN = len(X1) - true_count

    #Precision 정밀도 : 모델이True로 예측한 데이터 중 실제로 True인 데이터 수
    Precision= TP / (TP + FP)

    #Recall 재현율 : 실제로 True인 데이터를 모델이 True라고 인식한 수
    Recall=TP / (TP + FN)
    #F1_Score
    F1_Score = 2*(Precision*Recall)/(Precision+Recall)

    print(round(F1_Score,4),"score")
    print(round(TP,4),"TP")
    print(round(FP, 4), "FP")
    print(round(FN, 4), "FN")