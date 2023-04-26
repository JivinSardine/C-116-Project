import cv2

# read the image
img = cv2.imread("/Users/michaes/Desktop/CodingSpace/WhiteHatJR Python/C-116 Camera/Project/solar-system.jpg")


# display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# add text below each planet
# Mercury
cv2.putText(img, "Mercury", (120, 680), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Venus
cv2.putText(img, "Venus", (350, 680), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Earth
cv2.putText(img, "Earth", (550, 680), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Mars
cv2.putText(img, "Mars", (780, 680), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Jupiter
cv2.putText(img, "Jupiter", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Saturn
cv2.putText(img, "Saturn", (300, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Uranus
cv2.putText(img, "Uranus", (500, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Neptune
cv2.putText(img, "Neptune", (700, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# save the image
cv2.imwrite("/Users/michaes/Desktop/CodingSpace/WhiteHatJR Python/C-116 Camera/Project/Solar_systemwithname.jpg", img)
img2 = cv2.imread("/Users/michaes/Desktop/CodingSpace/WhiteHatJR Python/C-116 Camera/Project/Solar_systemwithname.jpg")


# display the final image
cv2.imshow("output", img2)
cv2.waitKey(0)
