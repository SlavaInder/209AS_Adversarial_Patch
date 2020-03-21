---
layout: default
---

# About
Recently within the past couple of years, adversarial attacks have gained a great amount of popularity in the realm of cyybersecurity. The goal of adversarial attacks is to fool standard machine learning models into misclassifying an input. The most common example of an adversarial attack is an image recognition model mislabelling an image of a panda as a "gibbon"[2]. 

<html>
  <body><p>
  <center><figure>
    <img src="https://miro.medium.com/max/2000/1*PmCgcjO3sr3CPPaCpy5Fgw.png" style = "max-width:80%">
    <center><figcaption>Adversarial Example</figcaption></center>
    </figure></center></p>
  </body>
</html>

This slight deviation, although unapparent to the human eye, can be reliably mounted against real-world computer vision systems, making it one of the most practical threat models against these machine learning systems. This type of threat model also can be performed without the attacker having direct access to the model itself. For example a sticker or a patch could fulfill the goal of confusing a classifier into mislabelling an object or image. The goal of our project is to translate robustness of these adversarial attacks into the real-world. Our project looks to fulfill the question of "Can a real-world adversarial attack be reliably mounted such that it is robust to the highly variant and unpredictable visual deformities of physical perturbations?" The focus of our project is to demonstrate the feasibility of such attacks and demonstrate an adversarial patch that is robust despite these conditions. 

<html>
  <body><p>
  <center><figure>
    <img src="images/adversarial_example.png" style = "max-width:80%">
    <center><figcaption>Physical Adversarial Attack</figcaption></center>
    </figure></center></p>
  </body>
</html>


# Today's Status and Novelty
Currently, there exists research papers detailing the adaptability of patches in a 2D environment. These include testing against translations, rotations, illuminations, and scaling. Despite the ventures within this area of adaptability, there does not exist a discussion of transformations equivalent nor similar to the concept of folds. Therefore, we look to present a new metric of patch transformation that will allow it to be transferrable to the real-world. This concept covers the basis that shirts, patches, stickers, and other non-rigid adversarial examples are subject to wrinkles or folds due to orientation of the product, posture of the individual wearing the product, or even ambient conditions such as wind. Additionally, the highly variant and unpredictable nature of this transformation makes it difficult to succinctly describe. Therefore, our project attempts to pose a modest solution to account for previously discussed transformations while also accounting for a newly described transform. 

<html>
  <body><p>
  <center><figure>
    <img src="https://netdna.coolthings.com/wp-content/uploads/2013/04/woolprince2.jpg" style = "max-width:80%">
    <center><figcaption>Examples of Wrinkles/Folds</figcaption></center>
    </figure></center></p>
  </body>
</html>

Based upon our research, we discovered a handful of papers that delve into creating real-world adversarial attacks for object detection models including adversarial hats, glasses, and clothes. Nevertheless, these papers did not detail the robustness of their products when subject to wrinkles, folds, or other visual oscurities. Although the paper "Adversarial T-shirt! Evading Person Detectors in A Physical World" [9] discusses the impact of cloth deformation, they overcame this issue with a digital image processing technique  called Thin Plate Splining (TPS) rather than an improvement of the patch itself. This algorithm essentially maps out the corners of the deformed shirt, transforms the input into a new plane, and smoothens out the image prior to classification. While this approach was successful in demonstrating the capabilities of adversarial T-shirts, it does not improve the adversarial model itself. Therefore, our project remains novel in exploring the impact of physical deformities that are likely to occur with these non-rigid, real-world adversarial attacks while also presenting the novel concept of folds as a transformation. Additionally, our experiment takes into account the previously described perturbations of translation, rotation, illumination, and scaling along with a folding factor to create a physically robust adversarial patch across previously researched variations as well. 
