# Face-Aging-with-conditional-GANs
An implementation of the paper title "Face Aging With Conditional Generative Adversarial Networks" by Grigory Antipov et al. An conditional GAN architecture is used in this project for automatic face aging. Significant steps include latent vector approximation with a Encoder for image recontruction. The novelty in the project is the "Identity Preserving" optimization of the latent space so that the latent vector retains the identity of the original image. This latent vector along with a conditioning vector which specifies the target age is used by the GAN to produce realistic projections of future or past facial images of an individual. 

## Architecture
![Architecture Diagram](https://www.oreilly.com/library/view/generative-adversarial-networks/9781789136678/assets/3019472f-d08b-4fa2-9ea1-071be37bc6bd.png)
