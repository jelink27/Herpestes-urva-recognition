# Herpestes-urva-recognition 
after watching 木曜四超玩-一日蟹農 \
影片中提到大閘蟹養殖戶常常半夜被食蟹獴襲擊\
導致嚴重損失，發想若能用攝影機結合影像辨識發出警告\
能讓養殖戶第一時間發現食蟹蒙入侵並即時做出反應

'''
uild a model to recognize the Herpestes urva \
在colab使用volov5訓練模型(x) \
初始模型使用28張照片，使用Lebalimg做Labeling \
使用Youtube影片做測試https://www.youtube.com/watch?v=qLKBstiddPc

'''
2022/12/7
新增image augmentation.py \
使用imgaug套件做image augmentation \
可將整個資料夾內影像讀入，產生五倍的訓練資料後存回資料夾 \
並依照原始檔案名稱後加註編號重新命名 

https://youtu.be/sJUsowjkM7g



