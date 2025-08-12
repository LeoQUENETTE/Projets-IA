import cv2


if __name__ == "__main__":
    image = cv2.imread("mon_image.png")

    if image is None:
        print("Erreur : impossible de charger l'image")
        exit()
    height, width = image.shape[:2]
    
    cv2.resize(image, None, fx=2,fy=2, interpolation=cv2.INTER_LINEAR)
    # ou
    cv2.resize(image,(8*width, 8*height), interpolation = cv2.INTER_CUBIC)
    cv2.imshow("Mon Image", image)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
