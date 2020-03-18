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

This slight deviation, although unapparent to the human eye, can be reliably mounted against real-world computer vision systems, making it one of the most practical threat models against these machine learning models. This type of threat model also can be performed without the attacker having direct access to the model itself. For example a sticker or a patch could fulfill the goal of confusing a classifier into mislabelling an object or image. 

# Today's Status and Novelty
Currently, there exists previous research papers detailing the adaptability of patches in a 2D environment. These include testing against translations, rotations, illuminations, and scaling. Additionally, there are works that delve into creating real-world use cases for object detection models. These examples include adversarial hats, glasses, and clothes, all of possess an adversarial characteristic to fool real-world computer vision systems. Unfortunately, these papers did not detail the robustness of their products when subject to wrinkles, folds, or other visual oscurities. Therefore, our project remains novel in exploring the impact of physical deformities that are likely to occur with these real-world adversarial attacks. Additionally, our experiment takes into account the previously described perturbations of translation, rotation, illumination, and scaling along with a folding factor to create a physically robust adversarial patch. 
