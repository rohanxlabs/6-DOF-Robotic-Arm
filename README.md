🤖 6-DOF Robotic Arm — AI-Powered Manipulation System

A fully modular and scalable 6 Degrees of Freedom (6-DOF) Robotic Arm system designed for simulation, perception, planning, and intelligent control.

This project demonstrates a complete robotics pipeline combining computer vision, motion planning, and kinematics, making it suitable for research, industrial automation, and AI-driven robotics applications.

---

🚀 Key Highlights

- 🦾 Full 6-DOF robotic arm control system
- 🎯 Forward & Inverse Kinematics implementation
- 🎥 Vision-based perception pipeline (AI-ready)
- 🧠 Modular architecture (Perception + Planning + Control)
- ⚙️ ROS / Simulation compatible design
- ✋ Integrated gripper control
- 📡 Real-time execution workflow
- 🔌 Easily extendable for AI & Reinforcement Learning

---

🏗️ System Architecture

                +----------------------+
                |     Perception       |
                |  (Camera + Detection)|
                +----------+-----------+
                           |
                           v
                +----------------------+
                |      Planning        |
                | (Mapping + Path Plan)|
                +----------+-----------+
                           |
                           v
                +----------------------+
                |       Control        |
                | (IK + Trajectory)    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     Robotic Arm      |
                |   (Execution Layer)  |
                +----------------------+

---

📁 Project Structure

6-DOF-Robotic-Arm/
│── main.py                     # Entry point of system
│
├── perception/                # Vision System
│   ├── camera.py              # Camera input handling
│   ├── detection.py           # Object detection logic
│   ├── view.py                # Visualization
│
├── control/                   # Motion Control
│   ├── kinematics.py          # FK & IK calculations
│   ├── trajectory.py          # Path interpolation
│   ├── gripper.py             # Gripper control
│
├── planning/                  # Planning Layer
│   ├── planner.py             # Motion planning
│   ├── mapping.py             # Environment mapping
│
├── utils/                     # Utilities
│   ├── config.py              # Configurations
│   ├── helpers.py             # Helper functions
│
└── requirements.txt

---

⚙️ Tech Stack

- Python
- ROS / ROS2 (optional integration)
- OpenCV
- NumPy
- MoveIt (for motion planning)
- Gazebo / RViz (simulation)

---

📦 Installation

1️⃣ Clone Repository

git clone https://github.com/rohanxlabs/6-DOF-Robotic-Arm.git
cd 6-DOF-Robotic-Arm

---

2️⃣ Create Virtual Environment

python -m venv venv

Activate:

- Windows:

venv\Scripts\activate

- Linux/Mac:

source venv/bin/activate

---

3️⃣ Install Dependencies

pip install -r requirements.txt

---

4️⃣ (Optional) ROS Setup

cd ~/catkin_ws
catkin_make
source devel/setup.bash

---

▶️ Usage

🔹 Run Complete System

python main.py

---

🔹 Run Individual Modules

Perception System

python perception/camera.py

Control System

python control/kinematics.py

Planning System

python planning/planner.py

---

🧠 Working Pipeline

1. Perception Layer

- Captures real-time camera feed
- Detects objects (extendable with AI models like YOLO)

2. Planning Layer

- Maps environment
- Computes optimal trajectory

3. Control Layer

- Solves inverse kinematics
- Generates joint movements

4. Execution Layer

- Sends commands to robotic arm
- Performs pick/place or manipulation

---

📊 Applications

- Industrial Automation
- Pick-and-Place Robotics
- AI-based Object Manipulation
- Robotics Research & Simulation
- Smart Manufacturing Systems

---

🔮 Future Enhancements

- 🤖 Reinforcement Learning for autonomous control
- 🎯 YOLO / SAM-based advanced perception
- 🗺️ SLAM-based environment mapping
- 🦾 Real hardware integration
- 🌐 Web dashboard / remote control system

---

📸 Demo (Add Your Media)

- 🎥 Add simulation video (recommended)
- 🖼️ Add system screenshots
- 📊 Add performance results

---

🤝 Contributing

Contributions are welcome and encouraged.

1. Fork the repository
2. Create your branch (feature/your-feature)
3. Commit your changes
4. Push to GitHub
5. Open a Pull Request

---

📜 License

This project is licensed under the MIT License.

---

👨‍💻 Author

RohanXLabs

- GitHub: https://github.com/rohanxlabs
- LinkedIn: (Add your profile link)

---

⭐ Support & Feedback

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork it
- 📢 Share with the community

---

💡 Note for Recruiters

This project demonstrates:

- Strong understanding of robotics fundamentals
- Practical implementation of kinematics & planning
- Ability to design modular AI-integrated systems
- Hands-on experience with real-world robotics pipelines

---