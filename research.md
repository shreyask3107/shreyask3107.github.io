---
layout: page
title: Research Proposals
subtitle: Few ideas to try out in future!
---


* **Transparent Reinforcement Learning:** Deep Reinforcement Learning(RL) is a powerful technique to train agents to carry out specific tasks. But we still do not know why an agent takes a bad action due to the non-interpretability of deep neural networks. Some recent works have been carried out on making RL agents' actions interpretable like [Object Sensitive Deep Reinforcement Learning](https://arxiv.org/abs/1809.06064) by Li et al. In this paper, the authors have used 'Object Saliency Maps' to obtain importance of particular objects for an agent to take an action. But they have implemented it in a video game 
setting where the background is already known when the object is removed. But in real world images we may not know the background and thus a Generative Advesarial Network(GAN) based method can be used to fill the background.

* **Imitation Learning with Observations:** In Imitation Learning, we need to give state, action pairs of an expert's demonstration. But in imitation learning in human beings, we do not get the action values while learning. Some of the recent works have been carried out by Liu et al. on [Imitation from Observation: Learning to Imitate Behaviors from Raw Video via Context Translation](https://arxiv.org/pdf/1707.03374.pdf). 


* **Reinforcement Learning for Block Sparsity Pruning in Deep Neural Networks for Model Compression:**
AutoML has been used for model compression to get smaller and faster deep neural networks by He et al[[1]](https://arxiv.org/pdf/1802.03494.pdf). But in this work they prune the weights with a reinforcement learning agent layer wise. But one of the better ways to achieve faster networks is by having block sparse weights. A reinforcement learning agent can be used to get block sparse weights.

* **Prediction of Intentions of Driver to Park a car:**
Many of the car companies have an automatic park feature which parks the car automatically. This does help the driver in making complex manoeuvres required to park the car in smaller spaces. But sometimes in cramped spaces like parking lots, the driver may make some wrong manoeuvres before pressing the auto park button. This may also make it diffcult for the decision system which governs the auto park action and thus not leading to a successful parking. To tackle this, a module could be added onto the vehicle to detect some features of the driver to detect his/her intentions to park the car. A few of the features that could be used are: The posture of the driver, the gaze of the driver, speed of the vehicle, steering directions. 
