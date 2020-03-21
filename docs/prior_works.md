---
layout: default
---

# Prior Works

<p>The idea of adversarial input attacks against image recognition systems was initially proposed in <a href="https://arxiv.org/pdf/1409.4842">[1]</a>. As stated in <a href="https://arxiv.org/pdf/1412.6572">[2]</a>, vulnerability to these attacks is a property shared among all "almost" linear high-dimensional systems. Initially, adversarial examples were constructed from images using gradient sign method: firstly gradient of the cost function over the input image, represented as a tensor, was calculated, and then a small step perturbed the image making probability of target class higher. This method allowed to make adversarial examples indistinguishable from real images (for human eye), but it also had some weak points. As such, image rotation, or change in brightess or view angle could severely reduce effect of the attack, and for it to perform well attacker had to have direct access to system input. In the following years extensive research was conducted on improving robustness of adversarial attacks. As such, in <a href="https://arxiv.org/pdf/1607.02533">[3]</a> an algorithm robust to small changes in brightness and angle was shown. One particularly interesting branch of this research is generating of adversarial patches: <a href="https://arxiv.org/pdf/1712.09665.pdf">[4]</a> shows, that successfull attack can be performed even if attacker changes only small part of the image, but in a way that is visible for human eye. This typpe of attack was shown to be robust against changes in scale, view angle, and brightness and was able to successfully fool recognition algorithms used in automated vehicles <a href="https://arxiv.org/pdf/1804.05810.pdf">[5]</a>, <a href="https://arxiv.org/pdf/1707.08945">[6]</a>. It was also proposed to use this types of attack against person detection algorithms by printing adversarial patches on glasses <a href="https://arxiv.org/pdf/1910.07067.pdf">[7]</a> or clothing <a href="http://openaccess.thecvf.com/content_CVPRW_2019/papers/CV-COPS/Thys_Fooling_Automated_Surveillance_Cameras_Adversarial_Patches_to_Attack_Person_Detection_CVPRW_2019_paper.pdf">[8]</a>. Our work builds upon this idea. To gain popularity as a print for different types of clothing, patches have to be robust against deformation that commonly happen in the process of wearing, such as folds or wrinkles. We aim to model these deformations and create a patch tolerant to them.</p>

<html>
  <body><p>
  <center><figure>
    <img src="https://braneshop.com.au/images/showreel/Evading%20Real-Time%20Person%20Detectors%20by%20Adversarial%20T-shirt.jpg" style = "max-width:80%">
    <center><figcaption>Adversarial T-shirt Example</figcaption></center>
    </figure></center></p>
  </body>
</html>
