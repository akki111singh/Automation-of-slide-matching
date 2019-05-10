### Automation-of-slide-matching  
      These days, the demand for online lectures is increasing. For better visual experience,
      along with the video of the lecture, soft copy of the slides is also being embedded into the
      video. But most of the universities are manually matching slides from the video to the soft
      copy which is a laborious task. So the problem statement is to automate this slide matching
      process.
      So to be more precise, you are given a set of noisy slide images extracted from the video and
      a set of slides from the original ppt. You need to build a mapping for each of the sampled
      noisy slides with the corresponding original slide.
      For example in the dataset given, consider the slides in any of the folders. You will see
      4-5 frames sampled from the lecture for which the corresponding ground truth slide is ppt.jpg.
      You may evaluate the performance of your algorithm on the given data. We would be
      testing on a more robust dataset.
      Also note that the sampled frames are almost aligned with the corresponding ground truth
      slide using homography.

# Prerequisites
    * OpenCV(4.1.0)
# How to run 
      * python3 cv.py <path/to/slides/directory> <path/to/frames/directory>
      * A txt file will be generated which contains a list of frames with their corresponding predicted slide name 
        separated by a single space.
        
 This is a team project along with @faixan-khan
      
