---
layout: default
---

# Future Direction
In conclusion, the results of our project demonstrated the ability to create an adversarial patch robust to the variant and unpredictable perturbations of the physical world. The possibility of mounting successful physical adversarial attacks are highly probable based upon our research and is applicable to the previously researched papers regarding physical adversarial attacks through the usage of hats, shirts, patches, stickers, and potentially even glasses. 

## Strengths
#### Adaptability of Adversarial Patches into the Real-World
The application of computer-vision systems are ever-growing and the use cases can extend beyond what we might consider as its limitations today. Currently, these machine learning models are mainly employed for security and protection purposes. Examples include people detection systems in museums, face recognition, self-driving cars, and more. An adversary could potentially bypass these systems utilizing the previously described physical adversarial attacks with the implementation of the detailed adversarial patch, rendering these security barriers ineffective. 

#### High Variability of Visual Deformities
In order to account for the unpredictability and variance of physical perturbations to adversarial items, all of the parameters were randomized within each session of our learning model. Therefore, we took into account a large range of potential folds, rotations, and shifts of the adversarial patch prior to inputting it in our Inceptionv3 model by utilizing a random number generator for every parameter. This includes the degree of rotation, the location of the folds, the size of the adversarial patch, and the shift/translation of the patch across the image.  

#### Introduction of A New Transformation
In order to demonstrate a patch robust to the conditions of the real-world, our model takes into account the possibility of folds or wrinkles. To the best of our knowledge, transformations previously described in other research papers do not take into account a perturbation equivalent nor similar to the folds detailed within our project. The removal of these pixels are a concept solely limited to a real-world perturbation and is unique to our overall project goal. 

## Limitations
#### Infinite Potential Visual Deformities
As stated previously, although our goal was to cover as many possible perturbations as possible, potential folds within the real-world vary in an infinite number of ways and are not contrained to a linear model. Additionally, our folding function does not account for the possibility of multiple folds within a single adversarial patch and rather evaluates them on a single-fold basis. Therefore, while it would be nearly impossible to account for every possible wrinkle, our project demonstrates the feasibility of creating a physical adversarial patch with a comparatively high success rate. 

#### Oblivious Classifier, Observant Humans
A previous point detailed an adversarial attack that can cause a classifier to mislabel an image yet look the same to the human eye. Unfortunately, this does not hold true with most real-world adversarial patches. Although these patches will fool a computer-vision system, the individuals wearing these adversarial examples can still be observed and recognized by others. Therefore in order to realistically and successfully mount an attack in the real-world, the physical adversarial example should be equally successful against computer-vision systems and to the regular human observer.

## Improvements to Future Iterations
Although our project demonstrates the possibility of mounting physical adversarial attacks against real-world computer vision systems, there remains room for improvement. A potential area of growth for the model would be the addition of multiple folds within the adversarial patch during training against the Inceptionv3 classifier. Despite the infinite possiblities that preside in the territory of multi-present folds, taking this matter into account at all significantly improves the robustness of the physical adversarial patch. Additionally, folds are not solely linear in nature and can be of any irregular shape or size. Therefore, by incorporating these unaddressed variables into the folding operation, our adversarial patch model can be significantly improved to cover a wider range of possibilities and in turn, greatly increase its success rate within the real-world

Another potential improvement would be to modify the visualization of the patch itself. Although our focus remains in the adaptability of the patch in the response to physical deformities, it remains relevant that the goal of any antagonist would be to break all measure of security for malicious intent. Therefore, while the real-world adversarial patch could consistently lead computer-vision systems into mislabelling, human observers will still be able to discern an attacker wearing these patches from a group of regular bystanders. In order to cover all bases, it would be a significant improvement to the overarching threat model to overcome this limitation as well. 
