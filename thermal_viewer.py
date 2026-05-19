import serial
import time
import numpy as np
import cv2

ser = serial.Serial('COM5', 115200)

time.sleep(2)

thermal_data = []

while True:

    try:

        line = ser.readline().decode('utf-8').strip()

        print(line)

        if line == "END":

            if len(thermal_data) == 24:

                img = np.array(thermal_data)

                img = cv2.resize(img, (640, 480))

                normalized = cv2.normalize(
                    img,
                    None,
                    0,
                    255,
                    cv2.NORM_MINMAX
                )

                colored = cv2.applyColorMap(
                    normalized.astype(np.uint8),
                    cv2.COLORMAP_JET
                )

                cv2.imshow("Thermal Camera", colored)

            thermal_data = []

        else:

            row = [float(x) for x in line.split(',')[:-1]]

            if len(row) == 32:
                thermal_data.append(row)

    except Exception as e:
        print("ERROR:", e)

    if cv2.waitKey(1) == ord('q'):
        break

ser.close()
cv2.destroyAllWindows()