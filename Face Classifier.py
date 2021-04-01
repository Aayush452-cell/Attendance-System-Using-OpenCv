import cv2

face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def face_extractor(img):
    faces = face_classifier.detectMultiScale(img, 1.3, 5)
    for (x, y, w, h) in faces:
        x = x - 10
        y = y - 10
        cropped_face = img[y:y + h + 50, x:x + w + 50]
        return cropped_face


cap = cv2.VideoCapture(0)
cnt = 0
while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        cnt += 1
        print("zq")
        face = cv2.resize(face_extractor(frame), (400, 400))
        file_name_path = './image/aayush/Images' + str(cnt) + '.jpg'
        cv2.imwrite(file_name_path, face)
        cv2.putText(face, str(cnt), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
        cv2.imshow('Face Cropped', face)
    else:
        print("Face Not Found")
        pass
    if cv2.waitKey(1) == 13 or cnt == 100:
        break

cap.release()
cv2.destroyAllWindows()
print("Collecting Sample Complete")
