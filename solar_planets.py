import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
            "Sun",
            (70,50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )
cv2.putText(img,
            "Mercury",
            (110,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )
cv2.putText(img,
            "Venus",
            (200,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )
cv2.putText(img,
            "Earth!",
            (290,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )
cv2.putText(img,
            "Mars",
            (400,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )
cv2.putText(img,
            "Jupiter",
            (500,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )
cv2.putText(img,
            "Saturn",
            (750,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )
cv2.putText(img,
            "Uranus",
            (975,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )
cv2.putText(img,
            "Neptune",
            (1100,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color = (255,255,255)
            )


cv2.imshow("Solar System",img)
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.waitKey(0)