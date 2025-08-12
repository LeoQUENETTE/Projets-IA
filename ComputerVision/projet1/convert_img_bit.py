import cv2

if __name__ == "__main__":
    image = cv2.imread("mon_image.png",cv2.IMREAD_GRAYSCALE)
     if image is None:
        print("Erreur : impossible de charger l'image")
        exit()