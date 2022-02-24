# Example code produced by CodingLikeMad on Youtube.
import cv2
import sys

def main():
    print(sys.argv[1])

    # Open the device in the first input argument, using the direct show backend.
    s_video = cv2.VideoCapture(int(sys.argv[1]), cv2.CAP_DSHOW )

    # For a full list of options the api is capable of, checkout:
    # https://docs.opencv.org/4.5.3/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    # Your camera may not be able to do everything on that list. For example, only cameras with focus control can change focus. Also, your camera may not impliment the entire
    # API, and then you won't be able to use all of it's features, even if it is physically capable of it.
    bright = 128    # How bright to set the camera image
    focus = 0       # Focal value for the camera.
    s_video.set(cv2.CAP_PROP_BRIGHTNESS, (bright))  # brightness (prop 10)
    s_video.set(cv2.CAP_PROP_FOCUS, (focus))  # Focus

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

        if key == ord('.'):
            focus = focus + 5
            s_video.set(cv2.CAP_PROP_FOCUS, (focus))  # Focus

        if key == ord(','):
            focus = focus - 5
            if focus < 0:
                focus = 0
            s_video.set(cv2.CAP_PROP_FOCUS, (focus))  # Focus

        if key == ord('='):
            bright = bright + 5
            s_video.set(cv2.CAP_PROP_BRIGHTNESS, (bright))

        if key == ord('-'):
            bright = bright - 5
            if bright < 0:
                bright = 0
            s_video.set(cv2.CAP_PROP_BRIGHTNESS, (bright))

# This is a test script which can help you identify which camera number is associated with the camera you are interested in. Each USB camera you have plugged in will get
# a distinct value here, and that value may change if you unplug another camera, or even plug them in in a different order. If this annoys you, contact microsoft, I am not
# responsible for their crummy device handling. It's awful.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('python camOptions.py <Cam Number>')
        print('Example code produced by CodingLikeMad on Youtube.')
        exit(-1)

    print('Use +/- and >/< keys(without shift) to adjust brightness and focus, respectively.')
    main()