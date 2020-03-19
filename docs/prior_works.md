---
layout: default
---

# Prior Works

<p>The idea of adversarial input attacks against image recognition systems was initially proposed in [1]. As stated in [2], vulnerability to these attacks is a property shared among all "almost" linear high-dimensional systems. Initially, adversarial examples were constructed from images using gradient sign method: firstly gradient of the cost function over the input image, represented as a tensor, was calculated, and then a small step perturbed the image making probability of target class higher. This method allowed to make adversarial examples indistinguishable from real images (for human eye), but it also had some weak points. As such, image rotation, or change in brightess or view angle could severely reduce effect of the attack, and for it to perform well attacker had to have direct access to system input. In the following years extensive research was conducted on improving robustness of adversarial attacks. As such, in [3] an algorithm robust to small changes in brightness and angle was shown. One particularly interesting branch of this research is generating of adversarial patches: [4] shows, that successfull attack can be performed even if attacker changes only small part of the image, but in a way that is visible for human eye. This typpe of attack was shown to be robust against changes in scale, view angle, and brightness and was able to successfully fool recognition algorithms used in automated vehicles [5], [6]. It was also proposed to use this types of attack against person detection algorithms by printing adversarial patches on glasses [7] or clothing [8]. Our work builds upon this idea. To gain popularity as a print for different types of clothing, patches have to be robust against deformation that commonly happen in the process of wearing, such as folds or wrinkles. We aim to model these deformations and create a patch tolerant to them.</p>


# References 
[1] Szegedy C. et. al, "Going deeper with convolutions", technical report, 2014.

[2] Goodfellow I. et al, "Explaining and Harnessing Adversarial examples", ICLR, 2015.

[3] Kurakin A. et al, "Adversarial attacks in physical world", ICLR, 2017.

[4] Brown T. et al, "Adversarial Patch", CVPR, 2017.

[5] Chen S.-T. et al, "ShapeShifter: Robust Physical Adversarial Attack on Faster R-CNN Object Detector", Joint European Conference on Machine Learning and Knowledge Discovery in Databases, 2018.

[6] Eykholt K. et al, "Robust Physical-World attacks on Deep Learning Visual Recognition", CVPR, 2018.

[7] Pautov M. et al, "On adversarial patches: real-world attack opn ArcFace-100 face recognition system", 2019.

[8] Thys S. et al, "Fooling automated surveillance cameras: adversarial patches to attack person detection", 2019.

## Image Sources
[1] Wrinkles: https://netdna.coolthings.com/wp-content/uploads/2013/04/woolprince2.jpg

[2] Pandas from "Explaining and Harnessing Adversarial Examples": https://miro.medium.com/max/2000/1*PmCgcjO3sr3CPPaCpy5Fgw.png

[3]
