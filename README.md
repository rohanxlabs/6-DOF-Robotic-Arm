<!-- Animated Header Banner -->
<div align="center">

```
██████╗      ██████╗  ██████╗ ███████╗
██╔════╝     ██╔══██╗██╔═══██╗██╔════╝
███████╗     ██║  ██║██║   ██║█████╗  
╚════██║     ██║  ██║██║   ██║██╔══╝  
███████║     ██████╔╝╚██████╔╝██║     
╚══════╝     ╚═════╝  ╚═════╝ ╚═╝     
  6-DOF Robotic Arm — rohanxlabs
```

# 🦾 6-DOF Robotic Arm

**A 6 Degrees-of-Freedom robotic arm simulation with Forward & Inverse Kinematics, trajectory planning, and ROS2 integration.**

[

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue?style=for-the-badge&logo=ros)

](https://docs.ros.org/en/humble/)
[

![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python)

](https://python.org)
[

![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

](LICENSE)
[

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

]()
[

![GitHub stars](https://img.shields.io/github/stars/rohanxlabs/6-DOF-Robotic-Arm?style=for-the-badge)

](https://github.com/rohanxlabs/6-DOF-Robotic-Arm/stargazers)

</div>

---

<!-- Demo GIF — replace with your actual recording -->
<div align="center">
  <img src="assets/demo.gif" alt="6-DOF Arm Demo" width="700"/>
  <br/>
  <em>↑ Replace this with a screen recording of your arm in action (Gazebo/RViz/real hardware)</em>
</div>

---

## 📌 Table of Contents

- [About](#-about)
- [Demo](#-demo)
- [Features](#-features)
- [Architecture](#️-architecture)
- [Kinematics](#-kinematics)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 About

This project implements a **6 Degrees-of-Freedom robotic arm** from scratch — covering the complete pipeline from mathematical modeling to simulation and (optionally) real hardware deployment.

Built as part of an ongoing exploration into **embodied AI**, **robot manipulation**, and the **sim-to-real pipeline**.

> **Why 6 DOF?**  
> 6 joints give a robot arm full positional and orientational freedom in 3D space — the minimum needed for general-purpose manipulation tasks.

---

## 🎬 Demo

<div align="center">

| Forward Kinematics | Inverse Kinematics | Trajectory Planning |
|:------------------:|:------------------:|:-------------------:|
| <img src="assets/fk_demo.gif" width="220"/> | <img src="assets/ik_demo.gif" width="220"/> | <img src="assets/trajectory.gif" width="220"/> |

> 💡 **To add your GIFs:** Record your terminal/simulation with [Peek](https://github.com/phw/peek) or [OBS](https://obsproject.com/), save to `assets/`, and replace the paths above.

</div>

---

## ✨ Features

```
✅  Forward Kinematics   — DH parameter-based FK solver
✅  Inverse Kinematics   — Geometric + analytical IK solver
✅  Trajectory Planning  — Joint-space interpolation
✅  Visualization        — RViz / Matplotlib 3D plots
✅  Simulation           — Gazebo integration (optional)
🔧  Hardware Interface   — Servo/stepper motor control (WIP)
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│               6-DOF Robotic Arm              │
├─────────────┬───────────────┬───────────────┤
│  Kinematics │   Planning    │   Interface   │
│             │               │               │
│  ┌────────┐ │ ┌───────────┐ │ ┌───────────┐ │
│  │   FK   │ │ │Trajectory │ │ │  ROS2     │ │
│  └────────┘ │ │Interpolate│ │ │  Node     │ │
│  ┌────────┐ │ └───────────┘ │ └───────────┘ │
│  │   IK   │ │ ┌───────────┐ │ ┌───────────┐ │
│  └────────┘ │ │ Collision │ │ │  Gazebo   │ │
│             │ │  Checking │ │ │  Sim      │ │
│             │ └───────────┘ │ └───────────┘ │
└─────────────┴───────────────┴───────────────┘
```

---

## 📐 Kinematics

### Denavit-Hartenberg Parameters

| Joint | θᵢ | dᵢ | aᵢ | αᵢ |
|:-----:|:--:|:--:|:--:|:--:|
| 1     | θ₁ | d₁ | 0  | 90° |
| 2     | θ₂ | 0  | a₂ | 0°  |
| 3     | θ₃ | 0  | a₃ | 90° |
| 4     | θ₄ | d₄ | 0  | -90°|
| 5     | θ₅ | 0  | 0  | 90° |
| 6     | θ₆ | d₆ | 0  | 0°  |

### Transformation Matrix (per joint)

$$
^{i-1}T_i = \begin{bmatrix}
\cos\theta_i & -\sin\theta_i\cos\alpha_i & \sin\theta_i\sin\alpha_i & a_i\cos\theta_i \\
\sin\theta_i & \cos\theta_i\cos\alpha_i & -\cos\theta_i\sin\alpha_i & a_i\sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

---

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.10+
python --version

# ROS2 Humble (optional, for ROS integration)
# https://docs.ros.org/en/humble/Installation.html

# Dependencies
pip install numpy matplotlib sympy
```

### Installation

```bash
# Clone the repository
git clone https://github.com/rohanxlabs/6-DOF-Robotic-Arm.git
cd 6-DOF-Robotic-Arm

# Install Python dependencies
pip install -r requirements.txt
```

---

## 🎮 Usage

### Run Forward Kinematics

```bash
python src/forward_kinematics.py --angles 0 45 -30 0 90 0
```

### Run Inverse Kinematics

```bash
python src/inverse_kinematics.py --target 0.3 0.1 0.5 --orientation 0 0 0
```

### Visualize in 3D

```bash
python src/visualize.py
```

### Launch with ROS2

```bash
# Source ROS2
source /opt/ros/humble/setup.bash

# Build
colcon build
source install/setup.bash

# Launch
ros2 launch arm_bringup arm_sim.launch.py
```

---

## 📁 Project Structure

```
6-DOF-Robotic-Arm/
│
├── src/
│   ├── forward_kinematics.py    # DH-based FK solver
│   ├── inverse_kinematics.py    # Geometric IK solver
│   ├── trajectory.py            # Joint-space trajectory planner
│   └── visualize.py             # 3D matplotlib visualization
│
├── ros2_ws/                     # ROS2 workspace (optional)
│   └── src/
│       └── arm_bringup/
│           ├── launch/
│           └── urdf/
│
├── assets/                      # GIFs, images, diagrams
│   ├── demo.gif
│   ├── fk_demo.gif
│   └── ik_demo.gif
│
├── tests/                       # Unit tests
├── requirements.txt
└── README.md
```

---

## 🗺️ Roadmap

```
[x] Forward Kinematics (DH Parameters)
[x] Inverse Kinematics (Geometric)
[x] 3D Visualization
[ ] MoveIt2 Integration
[ ] Gazebo Simulation
[ ] Pick-and-Place Task
[ ] Real Hardware (Servo/Stepper)
[ ] LLM-based task planning (SayCan-style)
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

```bash
# Fork → Clone → Branch → PR
git checkout -b feature/your-feature-name
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with 🤖 by [rohanxlabs](https://github.com/rohanxlabs)

⭐ **Star this repo if you find it useful!**

</div>