import cv2



from skimage.feature import greycomatrix, greycoprops


def glfeature(img):
    xs=[]
    img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)

    glcm = greycomatrix(img, [5], [0], 256, symmetric=True, normed=True)
    xs.append(greycoprops(glcm, 'contrast')[0,0])
    xs.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    xs.append(greycoprops(glcm, 'homogeneity')[0, 0])
    xs.append(greycoprops(glcm, 'ASM')[0, 0])
    xs.append(greycoprops(glcm, 'energy')[0, 0])
    xs.append(greycoprops(glcm, 'correlation')[0, 0])
    # print("xssssssssssssss",xs)
    return xs

