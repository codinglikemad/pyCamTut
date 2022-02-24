# Example code produced by CodingLikeMad on Youtube.
import cv2
import sys

def main():
    print(sys.argv[1])

    # Open the device in the first input argument, using the direct show backend.
    s_video = cv2.VideoCapture(int(sys.argv[1]), cv2.CAP_DSHOW )

    # continuely read and display frames
    while True:

        # Grab a frame from the device. This will wait until a frame is ready at this part of the code.
        ret, img = s_video.read()

        # Throw the frame onto a window - note that the name here matters and associated with an already open window
        cv2.imshow("Stream Video",img)

        # Wait for 1 ms on this frame. The output here is any keys hit - hit q to exit. You can of course do other things here like save the output.
        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            s_video.release() # Release the webcam. If you forget to do this or the code crashes, in the worst case you may need to unplug the USB camera or even reboot to free the device.
            break

# This is a test script which can help you identify which camera number is associated with the camera you are interested in. Each USB camera you have plugged in will get
# a distinct value here, and that value may change if you unplug another camera, or even plug them in in a different order. If this annoys you, contact microsoft, I am not
# responsible for their crummy device handling. It's awful.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('python testCam.py <Cam Number>')
        print('Example code produced by CodingLikeMad on Youtube.')
        exit(-1)
    main()