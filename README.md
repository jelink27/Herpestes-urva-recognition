# Herpestes-urva-recognition
after watching 木曜四超玩-一日蟹農 ,build a model to recognize the Herpestes urva
'''
在colab使用volov5訓練模型(x)
初始模型使用28張照片，使用Lebalimg做Labeling
使用Youtube影片做測試https://www.youtube.com/watch?v=qLKBstiddPc

'''
2022/12/7
新增image augmentation.py \
使用imgaug套件做image augmentation \
可將整個資料夾內影像讀入，產生五倍的訓練資料後存回資料夾 \
並依照原始檔案名稱後加註編號重新命名 \



