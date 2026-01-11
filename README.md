# AI-Assisted RTO Driving Test Evaluation System

## 📌 Project Overview
This project presents a **low-cost, AI-assisted RTO Driving Test Evaluation System** designed to objectively assess driving performance in a real-world RTO test environment.  
The system integrates **IoT-based camera modules, computer vision, Django backend services, and PostgreSQL database** to generate transparent and evidence-backed driving test results.

The project focuses on **system-level integration and real-time evaluation**, rather than proposing new machine learning algorithms.

---

## 🎯 Objectives
- Minimize subjectivity in manual RTO driving test evaluations
- Provide consistent and rule-based assessment
- Support low-cost prototype implementation
- Store results and evidence in a structured database
- Enable scalable and auditable evaluation using web technologies

---

## 🛠 Final System Design

### Camera Setup (Optimized & Practical)
- **Camera 1 – Vehicle-Mounted ESP32-CAM**
  - Lane discipline evaluation
  - Traffic signal compliance (logic-based)
  - Parking evaluation

- **Camera 2 – Fixed Turning-Point ESP32-CAM**
  - Indicator usage (left/right)
  - Turn execution compliance

### Security Verification
- Candidate identity verification is handled **manually via application by a monitoring person**
- No automated face recognition during the driving test

---

## 🔄 Working Methodology
1. Candidate verification completed through application
2. Driving test initiated by RTO monitor
3. Vehicle-mounted camera streams video for lane and signal analysis
4. Turning-point camera evaluates indicator usage
5. Parking behavior evaluated using vehicle camera
6. AI models generate detections from video streams
7. Rule-based logic evaluates compliance
8. Results and evidence stored in database
9. Final score and pass/fail status displayed on dashboard

---

## 🧠 Technology Stack

### Backend
- **Django** – Web framework for APIs and system logic
- **Django REST Framework (DRF)** – RESTful API development
- **PostgreSQL** – Relational database for storing test data, logs, and results

### AI & Computer Vision
- **Python**
- **OpenCV** – Video processing and feature extraction
- **PyTorch** – AI model inference

### IoT & Communication
- **ESP32 / ESP32-CAM**
- **Wi-Fi** – Video streaming and data transmission
- **HTTP / RTSP** – Stream handling

---

## 🗄 Database Design (PostgreSQL)
- Candidate details
- Test session records
- Camera event logs
- Rule violations
- Scoring metrics
- Evidence metadata (video/image paths)

---

## 🤖 AI & Rule-Based Components
- Lane detection using computer vision
- Traffic signal detection using vehicle camera
- Indicator detection at turning point
- Parking alignment evaluation
- Rule-based decision engine for pass/fail determination

---

## ✅ Key Features
- Real-time evaluation in actual test environment
- Django-based backend for scalability
- Structured PostgreSQL storage
- Evidence-backed decisions
- Low-cost and modular prototype design

---

## 🚧 Limitations
- Prototype relies on laptop for AI processing
- Performance depends on lighting and camera placement
- Controlled RTO test environment assumed

---

## 🔮 Future Enhancements
- Edge inference optimization
- Multi-camera synchronization
- Advanced analytics dashboard
- Integration with official RTO systems
- Cloud deployment for large-scale adoption

---

## 📚 Academic Note
This project emphasizes **practical system integration of AI, IoT, and web technologies** for governance applications.  
The novelty lies in **architecture and real-world deployment**, not in developing new machine learning models.

---

## 👨‍🎓 Author
**Name:** Your Name  
**Register Number:** Your Registration Number  
**Guide:** Dr. Guide Name  

---

## 📄 License
This project is intended for **academic and research purposes only**.
