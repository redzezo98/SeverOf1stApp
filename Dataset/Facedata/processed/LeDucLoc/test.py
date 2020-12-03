import cv2
for i in range(1,22):
    number = i
    img = cv2.imread(f'{number}.png',cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f'Thu{number}.png', img)
