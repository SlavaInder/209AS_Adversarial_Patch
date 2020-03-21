---
layout: default
---
# Metrics
In order to determine how successful our patches were, we collected a concrete set of metrics for comparison. Per patch size and thickness, we measured:
- Lowest accuracy: lowest accuracy measurement of the target class (misclassified class)
- Top-5 accuracy: number of images that produced the target class within its top 5 probabilistic measurements
- Average accuracy: average accuracy measurement of the target class across the entire dataset

For clarification, for the purposes of our project, accuracy is considered the probability that the classifier would mislabell the input image. Additionally, it is important to note that our results are inherently probabilistic. Therefore, repeated trials of our experiment are likely to yield similar, but not duplicate results. 

# Results
<html>
  <body><p>
  <center><figure>
    <img src="images/result_adv.png" style = "max-width:70%">
    <center><figcaption>Resulting Adversarial Patch with Fold</figcaption></center>
    </figure></center></p>
  </body>
</html>

<html>
  <body><p>
  <center><figure>
    <img src="images/table1.png" style = "max-width:100%">
    <center><figcaption>Patch Size vs. Accuracy Metrics with 10% Folds</figcaption></center>
    </figure></center></p>
  </body>
</html>

<html>
  <body><p>
  <center><figure>
    <img src="images/avg_acc.png" style = "max-width:70%">
    <center><figcaption>Patch Size vs Average Accuracy</figcaption></center>
    </figure></center></p>
  </body>
</html>

<html>
  <body><p>
  <center><figure>
    <img src="images/top_acc.png" style = "max-width:70%">
    <center><figcaption>Patch Size vs Top-5 Accuracy</figcaption></center>
    </figure></center></p>
  </body>
</html>

Based upon the tables and plots above, it was seen that the 150x150 patch demonstrated the highest performance. Therefore, we focused on this patch size and looked to determine the impact of the size of folds on the accuracy metrics of the patch.

<html>
  <body><p>
  <center><figure>
    <img src="images/table2.png" style = "max-width:100%">
    <center><figcaption>10%-40% Folds (150x150 patches) vs Accuracy Metrics</figcaption></center>
    </figure></center></p>
  </body>
</html>


# Evaluation
Based upon our results, we demonstrate the feasibility of creating an adversarial patch robust to folds, rotations, translations, and scaling. Overall our adversarial patch does not 
