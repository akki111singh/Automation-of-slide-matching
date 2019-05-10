import numpy as np
import cv2
import os, sys, os.path
from matplotlib import pyplot as plt


sift = cv2.xfeatures2d.SIFT_create()



slide_path = sys.argv[1]
frame_path = sys.argv[2]
slide_len = len([name for name in os.listdir(slide_path) if os.path.isfile(os.path.join(slide_path, name))])
frame_len = len([name for name in os.listdir(frame_path) if os.path.isfile(os.path.join(frame_path, name))])
text_file = open("20171209_20171210.txt", "w")


frames = os.listdir(frame_path)
slides = os.listdir(slide_path)
frames.sort()
slides.sort()

# for i in range(len(frames)):
#     print(frames[i])
# 	# frames[i] = "./frames/" + frames[i]

# for i in range(len(slides)):
#     print(slides[i])
	# slides[i] = "./slides/" + slides[i]

# print(str(frame_path)+str(frames[1])) 
for img in range(len(frames)):
    ind_slide = 0
    ind_frame = 0
    maxi = 9999999
    for j in range(len(slides)):
        # print(img)
        # print(frame_path+'/'+str(frames[img]))   
        # print(slide_path+'/'+str(slides[j]))
        img1 = cv2.imread(str(frame_path)+'/'+str(frames[img]),0)         
        img2 = cv2.imread(str(slide_path)+'/'+str(slides[j]),0) 


        sift_1, desc_1 = sift.detectAndCompute(img1,None)
        sift_2, desc_2 = sift.detectAndCompute(img2,None)

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=100)   

        flann = cv2.FlannBasedMatcher(index_params,search_params)

        features = flann.knnMatch(desc_1,desc_2,k=2)

        matchesMask = [[0,0] for i in range(len(features))]

        not_so_good = 0
        for i,(m,n) in enumerate(features):
            if m.distance < 0.5*n.distance:
                matchesMask[i]=[1,0]
            else:
                not_so_good = not_so_good + 1

        draw_params = dict(matchColor = (0,255,0),singlePointColor = (255,0,0),matchesMask = matchesMask,flags = 0)

 

        # img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
        # plt.imshow(img3,),plt.show()

        # print(frame_len)
        # print(frames[img])
        if(not_so_good <= maxi):
            
            maxi = not_so_good
            ind_frame = frames[img]
            ind_slide = slides[j]
    # print(not_so_good)

    # print( str(ind_frame)+'.jpg '+'ppt'+str(ind_slide)+'.jpg')
    text_file.write(str(ind_frame)+' '+str(ind_slide))
    text_file.write('\n')

# text_file.write("Purchase Amount: %s" % TotalAmount)
text_file.close()
# 8.jpg ppt1.jpg
# 9.jpg ppt1.jpg
