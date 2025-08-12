import cv2


if __name__ == "__main__":
    image = cv2.imread("mon_image.png")

    if image is None:
        print("Erreur : impossible de charger l'image")
        exit()
    
    cv2.imshow("Mon Image", image)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
