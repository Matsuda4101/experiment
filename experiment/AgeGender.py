# -*- coding: utf-8 -*-
import cv2 as cv
import time
import argparse

def getFaceBox(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn, bboxes

def crop_center(pil_img):
    img_height, img_width = pil_img.shape[:2]
    img1 = pil_img[100:500,100:500]
    return img1

def face_age():
    parser = argparse.ArgumentParser(description='Use this script to run age and gender recognition using OpenCV.')
    parser.add_argument('--input', help='Path to input image or video file. Skip this argument to capture frames from a camera.')
    parser.add_argument("--device", default="cpu", help="Device to inference on")

    args = parser.parse_args()
    args = parser.parse_args()

    faceProto = "age/opencv_face_detector.pbtxt"
    faceModel = "age/opencv_face_detector_uint8.pb"

    ageProto = "age/age_deploy.prototxt"
    ageModel = "age/age_net.caffemodel"

    genderProto = "age/gender_deploy.prototxt"
    genderModel = "age/gender_net.caffemodel"

    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
    ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
    genderList = ['Male', 'Female']

    # Load network
    ageNet = cv.dnn.readNet(ageModel, ageProto)
    genderNet = cv.dnn.readNet(genderModel, genderProto)
    faceNet = cv.dnn.readNet(faceModel, faceProto)

    if args.device == "cpu":
        ageNet.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)

        genderNet.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)
    
        faceNet.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)

        print("Using CPU device")
    elif args.device == "gpu":
        ageNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
        ageNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

        genderNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
        genderNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

        genderNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
        genderNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)
        print("Using GPU device")


    enter = cv.imread("age/images/Enter.png")
    b, g, r = cv.split(enter)
    enter = cv.merge([r,g,b])
    e_h, e_w = enter.shape[:2]
    enter = cv.resize(enter, dsize=(300,int(e_h*(300/e_w))))
    e_h, e_w = enter.shape[:2]

    #maru = cv.imread("face/maru.png")
    #b, g, r = cv.split(maru)
    #maru = cv.merge([r,g,b])

    # Open a video file or an image file or a camera stream
    cap = cv.VideoCapture(args.input if args.input else 0)
    padding = 20
    while True:
        # Read frame
        t = time.time()
        hasFrame, frame = cap.read()
        #if not hasFrame:
            #cv.waitKey()
            #break
        
        frame = cv.flip(frame, 1)

        frame = crop_center(frame)
        frame1 = frame
        #frame1[0:e_h,0:e_w] = enter
        cv.imshow("Camera", frame1)

        #hwnd = win32gui.GetActiveWindow()
        #(x, y, w, h) = cv.getWindowImageRect("Age Gender Demo")
        #win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, w, h, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # cv.imwrite("age-gender-out-{}".format(args.input),frameFace)
        # print("time : {:.3f}".format(time.time() - t))
        if cv.waitKey(1) > 0:
            cap.release()
            cv.destroyAllWindows()
            break
    return frame

#if __name__ == '__main__':
    #f = face_age()
    # print(a)
    # print(f)
    #cv.imshow("fashion image",f)
    #cv.waitKey(0)
    #cv.destroyAllWindows()