import cv2
import os

# Label: 00000 là ko cầm tiền, còn lại là các mệnh giá
# label = "00000"
# label = '10000'
# label = '200000'
label = '500000'

cap = cv2.VideoCapture(0)

# Biến đếm, để chỉ lưu dữ liệu sau khoảng 60 frame, tránh lúc đầu chưa kịp cầm tiền lên
i = 0
while True:
    # Capture frame-by-frame
    #
    i += 1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None, fx=0.3, fy=0.3)

    # Hiển thị
    cv2.imshow('frame', frame)

    # Lưu dữ liệu
    if i >= 60 and i < 250 + 60:
        print('anh thu: ', i-59)
        # Tạo thư mục nếu chưa có
        if not os.path.exists('data/' + str(label)):
            os.mkdir('data/' + str(label))

        cv2.imwrite('data/' + str(label) + "/" + str(i-59+250) + ".png", frame)

    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()