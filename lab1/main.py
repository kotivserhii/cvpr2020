import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output1.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv.imshow('Original', frame)
    if cv.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

cap2 = cv.VideoCapture('output1.avi')
fourcc2 = cv.VideoWriter_fourcc(*'XVID')
out2 = cv.VideoWriter('output2.avi', fourcc2, 30.0, (640, 480))
frames_counter = 1
while(cap2.isOpened()):
    frames_counter = frames_counter + 1
    ret, frame = cap2.read()
    if ret == False:
        break
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.cvtColor(frame, cv.COLOR_GRAY2RGB)

    cv.rectangle(frame_gray, (100, 50), (200, 300), (0, 0, 255), -1)
    cv.circle(frame_gray, (250, 250), 100, (0, 0, 255), -1)
    out2.write(frame_gray)
    cv.imshow('frame', frame_gray)
    if cv.waitKey(25) == ord('q'):
        break
print("Number of frames in the video: ", frames_counter)
cap2.release()
out2.release()
cv.destroyAllWindows()