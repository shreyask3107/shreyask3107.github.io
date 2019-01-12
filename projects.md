---
layout: page
title: My Projects
subtitle: A few of my projects
---

### Reinforcement Learning for Image Quality Improvement for Object Detection:
#### Author: **Siddharth Nayak, Manan Tomar, Rahul Ramesh, Balaraman Ravindran**

#### Abstract: **Object Detection performance for a deep network depends a lot on the image quality. Generally images are preprocessed by motion de-blurring, gaussian blurring to remove noise, etc. Not quite a lot of work has been done before on improving the images at the time of it getting captured. A photographer while taking images changes a lot of parameters like shutter speed, gains, aperture to get the best image. Bychkovsky et al[[1]](http://people.csail.mit.edu/vladb/photoadjust/db_imageadjust.pdf). worked on training a network to come up with image retouches which look pleasing to a human by training it on a dataset which was digitally annotated by expert photographers using photoshop. Yang et al[[2]](https://arxiv.org/pdf/1803.02269.pdf). worked on using reinforcement learning to get user based adaptive exposure control to come up with good shutter speeds to capture good images which looked pleasing to humans. This project aims towards making a camera capture images in real-time which are good for a given object detection neural network to increase its performance.** [**[PDF]**](https://drive.google.com/file/d/1RDYVBnBJZoxxKoaK5inetT7FC4paKiWF/view?usp=sharing) [**[Code]**](https://github.com/nsidn98/Reinforcement-Learning-for-Object-Detection)

### Robust Reinforcement Learning:
#### Author:**Rishhanth Maanav V and Siddharth Nayak**

#### Abstract: **Reinforcement Learning agents have been used for a wide range of tasks, such as games and robotic control. The agent tries to learn policies and value functions through trial and error by interacting with the environment until it converges to an optimal policy. Robustness and stability are quite critical in Reinforcement Learning; however, neural networks are vulnerable to noise from unexpected sources and are not likely to withstand disturbances. Also, whenever robots are trained with Reinforcement Learning agents, they are generally either initialized with hand-made policies or policies from simulated agents. The simulated agents,however may not capture all of the noise in a real-world robot. Thus, the transfer learning may not be efficient enough for faster convergence on robots. In this paper we evaluate two robust reinforcement learning algorithms and compare them along with the vanilla algorithm and a naive algorithm described further in the paper. The main idea in this paper is that we can use adversarial examples to choose perturbations duringthe training of the agent. In this paper we try to implement the robust reinforcement learning algorithmssimulated in OpenAI Gym and MujoCo Environments with perturbations in the observations. We use the Reacher-V2 environment of OpenAI Gym with MujoCo backend for our evaluation.**
[**[PDF]**](https://drive.google.com/file/d/1fzDxQJYzN-v4l-awmIjove0WJ48IAj6u/view?usp=sharing)[**[Code]**](https://github.com/nsidn98/Robust-Reinforcement-Learning)

### Hand Gesture Recognition for Soldier Support:
#### Author: **Siddharth Nayak**

**Abstract:** Soldiers communicate with each other through gestures. But sometimes those gestures are not visible due to obstructions or poor lighting. For that purpose an instrument is required to record the gesture an send it to the fellow soldiers. The two options for gesture recognition are through Computer Vision and through some sensors attached to the hands.The first option is not viable in this case as proper lighting is required for recognition through Computer Vision. Hence the second option of using sensors for recognitions has been used. We present a system which recognises the gestures given in this [link](https://github.com/nsidn98/Gesture-Recognition/blob/master/Images/gestures.jpg).
[**[Documentation]**](https://github.com/nsidn98/Gesture-Recognition/blob/master/README.md)[**[Code]**](https://github.com/nsidn98/Gesture-Recognition)

### Automatic Waste Segregation Dustbin:
#### Project Members: **Varun Sundar, Arvind Pujari, Siddharth Nayak, Rohith Srinivas, Vishnu Harshith, Sai Venkat, Iniyan Ram**
India produces an average of 0.5 kilograms of waste, per person, every day. With a population of over 1.2 billion, this translates to an overwhelming amount of Muncipal Solid Waste (MSW) being produced. However, there is virtually no segregation at source in India, hence most waste is dumped directly into landfills. This leads to huge piles of waste and poor living standards for ragpickers and those in the vicinity. It also leads to groundwater pollution, the effects of which can percolate to hundreds of kilometers. If the issue of waste segregation in India is not solved in the near future, there will be a point after which landfills cannot accommodate anymore waste, leading to overflowing of landfills, and accumulation of waste in urban areas, which will lead to serious health and sanitary problems, making cities almost uninhabitable.
Hence, the development of technology for segregation at source is necessary. In the present study, we explore one possibility, in the form of self segregating dustbins, which uses deep learning on features based on vision,inductance and capacitance, coupled with a mechanical sorting system, to identify and classify waste into distinct categories, and segregate it at source.
[**[Documentation]**](https://drive.google.com/file/d/178VnadP2o9sCO6stPFOkq8jVb0PkeQId/view?usp=sharing)


### Self- Balancing Robot
#### Project Members: **Siddharth Nayak, Rahul Chakwate, Adil Shaikh, Anuj Sindgi, Atharva Rajadnya**
(My first tech project.)


### Mini Projects:
#### A list of small projects which required less than a week to work on:
* [**DeepTraffic**](https://selfdrivingcars.mit.edu/deeptraffic/) is a deep reinforcement learning competition. The goal is to create a neural network to drive a vehicle (or multiple vehicles) as fast as possible through dense traffic. I got a rank of 3203 out of 24,449 participants with a speed of 69.18 mph.[**[Code]**](https://github.com/nsidn98/DeepTraffic-MIT)

* **MouseCam**: MouseCam is a small device I made to control a computer mouse with our thumb, index and middle finger. There are two ways to control the mouse:
  - Control with a webcam which will detect fingers and track them according to colors. This requires a person to wear small wearables of different colors on their fingers. 
  - Control with the device which has an Inertial Measurement Unit and push buttons to control the motion of the mouse pointer. 
The mouse is basically controlled with the movement of the hand. The mouse pointer almost mimics the movement of the hand. [**[Code]**](https://github.com/nsidn98/Mouse-cam)

* **Music with Numbers**: I like to play piano when I am bored or want to cheer myself. I was intrigued by Beethoven's music and saw a video about the math behind some of his musical masterpieces. So I wrote a small piece of code to convert the first few digits of ![pi](http://latex.codecogs.com/gif.latex?%5Cpi) and ![e](http://latex.codecogs.com/gif.latex?e) to music on different pentatonic scales. Different scales can be chosen to make the music with numbers. Here are examples of music generated from [pi](https://drive.google.com/file/d/1xqlR9W704Lurq1qHxuNgQ2DjXlNhA3L8/view?usp=sharing) and [e](https://drive.google.com/file/d/1BCA1s1jsqApCm0oZtBV60-okhJHtmDkn/view?usp=sharing). [**[Code]**](https://github.com/nsidn98/Music-with-numbers)

* **Games**: A few of the games implemented 
  - Conway's Game of Life
  - Car Racer
  - Maze Solver: Solves mazes with input image
  [**[Code]**](https://github.com/nsidn98/Games)
