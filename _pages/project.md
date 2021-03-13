---
layout: archive
title: "A few of the projects I worked on!"
permalink: /project/
author_profile: true
redirect_from:
  - /extracurricular-activities
---
## Residual Policy Learning(2020)
*Authors: [Antonia Bronars](https://www.linkedin.com/in/antonia-bronars-a6ab17112/), [Rebecca Jiang](https://www.linkedin.com/in/rebecca-jiang/), Siddharth Nayak*

A course project for the [6.881-Robotic Manipulation](http://manipulation.csail.mit.edu/Fall2020/) Fall 2020 course at MIT by [Prof. Russ Tedrake](https://groups.csail.mit.edu/locomotion/russt.html). We worked on implementing a controller plus reinforcement learning agent to improve the sample efficiency of reinforcement learning (RL) agents for robotic tasks with sparse rewards (residual learning). We design controllers for the mujoco push, pick-and-place and sliding tasks robosuite pick-and-place and peg-in-hole tasks each with different task success rates. We train reinforcement learning agents on top of these controllers to improve the success rates of the agents. We compare this against learning an RL agent from scratch and show that residual learning has better sample efficiency. This project was an implementation of the Residual Policy Learning paper by Silver et al. [[PDF]](https://nsidn98.github.io/files/residualPolicyLearning.pdf) [[Code]](https://github.com/nsidn98/Residual-Policy-Learning)

## PyThor (2020)
*Author: Siddharth Nayak*

A side project of mine where I try to combine PyTorch, Pytorch-lightning, Telegrad and MLFlow for ML-based projects. I took this up when I was in the pandemic-lockdown  and was waiting for my graduate school to start. The pytorch-lightning module takes care of the boilerplate code in running experiments. Telegrad gives live updates(when requested) about the status of the training losses along with plots on your mobile so that you can monitor your jobs on the go while you are not on your system. You can also chage the learning rates from your mobile. MLFlow manages the experiments so that each experiment can be reproduced by logging in all the hyper-parameters used. Have provided some template codes for linear, convolutional and graph networks along with some reinforcement learning examples. This was basically done by me as a preparation for my graduate school codebases.[[Code]](https://github.com/nsidn98/PyThor)

## Transfer Matching Networks (2019)
*Authors: [Abhishek Nair](https://abhisheknair1729.github.io/) and Siddharth Nayak*

A course project for the [EE6180-Advanced Topics in Artificial Intelligence](https://home.iitm.ac.in/abhishek.sinha/teaching_ML.html) (Fall 2019) course by [Prof. Abhishek Sinha](https://home.iitm.ac.in/abhishek.sinha/) at IIT Madras. We tried to add a autoencoder module in the reinforcement learning pipeline to help with domain randomisation. As this was a 3-week project, we did not get to investigate the problem as much as we wanted. [[Final Presentation]](https://nsidn98.github.io/files/Transfer_Matching_Networks_Presentation.pdf) [[Code]](https://github.com/nsidn98/Transfer-Learning-for-RL)

## Robust Reinforcement Learning (2018)
*Authors: [Rishhanth Maanav V](https://github.com/rishi307) and Siddharth Nayak*

A project done as a course project for the [CS6700-Reinforcement Learning](http://www.cse.iitm.ac.in/~prashla/cs6700_2021.html) course at IIT Madras by [Prof. L.A. Prashanth](http://www.cse.iitm.ac.in/~prashla/). We implement two robust reinforcement learning algorithms: Robust Adversarial Reinforcement Learning (RARL) by Pinto et al. and Adversarial Robust Policy Learning (ARPL) by Mandlekar et al. and compare them with na&iuml;ve and vanilla reinforcement learning algorithms under various amounts of perturbations to the model dynamics.
[[PDF]](http://nsidn98.github.io/files/RobustRL.pdf) [[Code]](https://github.com/nsidn98/Robust-Reinforcement-Learning)

## Hand Gesture Recognition for Soldier Support (2017-18)
*Author: Siddharth Nayak*

I created a hand-gesture recognition glove which recognises the gestures given in this [link](https://github.com/nsidn98/Gesture-Recognition/blob/master/Images/gestures.jpg). This does not use computer vision and instead uses readings from sensors attached to the glove. 
[[PDF]](http://nsidn98.github.io/files/Gesture_Recognition.pdf) [[Documentation]](https://github.com/nsidn98/Gesture-Recognition/blob/master/README.md) [[Code]](https://github.com/nsidn98/Gesture-Recognition)

## Automatic Waste Segregation Dustbin (2017)
*Project Members: Varun Sundar, Arvind Pujari, Siddharth Nayak, Rohith Srinivas, Vishnu Harshith, Sai Venkat, Iniyan Ram*

We created an automatic waste segregation dustbin which classifies the waste into distinct categories using features learned from images, the capacitances and the inductances of the waste. The dustbin also has a mechanical disc powered by stepper motors which push the waste into its corresponding compartment after the classification.
[[Documentation]](http://nsidn98.github.io/files/AWS.pdf)


## Self-Balancing Robot (2016-17)
*Project Members: Siddharth Nayak, Rahul Chakwate, Adil Shaikh, Anuj Sindgi, Atharva Rajadnya*

Self-Balancing Robot was the first tech-project I worked on. It is basically a one wheeled robot which balances itself to stay upright. It is like the real-life version of the Cartpole from OpenAI Gym. The robot balances itself using a tuned Proportional-Integral-Derivative(PID) Controller. The angles of inclination and the angular velocities are given as the state vector. I learnt a lot about electronics, robotics and programming while working on this project.[[Code]](https://github.com/nsidn98/One-Wheeled-Balancing-Robot)


## Mini Projects:
****************************************
### A list of small projects which required less than a week to work on:
* [**Bass Booster**](https://github.com/nsidn98/Bass-Treble-Booster): A pythonic way to overlay another layer of bass in audio files. I was motivated to try out this after hearing this [bass boosted version](https://www.youtube.com/watch?v=VmITSg23CTY) of Attention by Charlie Puth. Can also work as a treble booster.

* [**DeepTraffic**](https://selfdrivingcars.mit.edu/deeptraffic/) was a deep reinforcement learning competition held at MIT as a part of the IAP course 6.S094. The goal is to create a neural network to drive a vehicle (or multiple vehicles) as fast as possible through dense traffic. I got a rank of 3203 out of 24,449 participants with a speed of 69.18 mph.[[Code]](https://github.com/nsidn98/DeepTraffic-MIT)

* **MouseCam**: MouseCam is a small device I made to control a computer mouse with our thumb, index and middle finger inspired by Tony Stark's hologram projection from the Iron Man movie. There are two ways to control the mouse:
  - Control with a webcam which will detect fingers and track them according to colors. This requires a person to wear small wearables of different colors on their fingers. 
  - Control with the device which has an Inertial Measurement Unit and push buttons to control the motion of the mouse pointer. 
The mouse is basically controlled with the movement of the hand. The mouse pointer almost mimics the movement of the hand. This was a precursor project to the gesture recognition system I made.[[Code]](https://github.com/nsidn98/Mouse-cam)

* **Music with Numbers**: I like to play piano when I am bored or want to cheer myself. I have always been intrigued by Beethoven's music. I came across a video about the math behind some of his musical masterpieces which inspierd me to write this small piece of code to convert the first few digits of ![pi](http://latex.codecogs.com/gif.latex?%5Cpi) and ![e](http://latex.codecogs.com/gif.latex?e) to music on different pentatonic scales. Different scales can be chosen to make the music with numbers. Here are examples of music generated from [pi](https://drive.google.com/file/d/1xqlR9W704Lurq1qHxuNgQ2DjXlNhA3L8/view?usp=sharing) and [e](https://drive.google.com/file/d/1BCA1s1jsqApCm0oZtBV60-okhJHtmDkn/view?usp=sharing). [[Code]](https://github.com/nsidn98/Music-with-numbers)

* **Games**: A few of the games implemented 
  - Conway's Game of Life
  - Car Racer: The video game of traversing a car through a road just like the DeepTraffic Competition.
  - Maze Solver: Solves mazes with input image
  [[Code]](https://github.com/nsidn98/Games)



  