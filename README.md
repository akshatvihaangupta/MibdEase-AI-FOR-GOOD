🧠 MindGuardians — Mental Health Check-In Portal
A practical prototype — not a medical diagnosis.
Build the bridge before the gap becomes a crisis.

A lightweight, explainable, rule-based mental health early detection portal for students. Built as a single-file Python prototype with no backend, no training data, and no diagnosis — just a fast, auditable way to flag who may need support.

📌 Table of Contents
The Problem

Our Approach

How It Works

Scoring Logic

Features

Tech Stack

Installation & Usage

File Structure

Screenshots / Flow

Roadmap

SDG Alignment

Important Disclaimer

Team

License

🚨 The Problem
The missing layer is not awareness — it's early, low-friction detection.

Students often wait until distress becomes visible. By then, the gap has already widened.

Challenge	Reality
Stigma	Students hesitate to ask for help
Academic pressure	Sleep disruption + isolation overlap silently
Reactive support	Institutions act only after a crisis
No structured signals	Counselors lack early, reviewable indicators
Evidence Snapshot
7.3% — Mental disorders among ages 13–17 (National Mental Health Survey 2015–16)

15% — Indian adults needing active intervention for one or more mental-health issues

$1.03 Trillion — Estimated economic loss in India from mental-health conditions (2012–2030)

Why Rule-Based AI?
✅ Explainable — every point maps to an explicit rule

✅ Auditable — counselors can inspect and revise thresholds

✅ Fast — runs instantly on any normal computer

✅ Human-in-the-loop — flags concern; people decide what happens next

✅ No training dataset required for the prototype

⚠️ Rule-based ≠ diagnosis.

⚙️ How It Works
1️⃣ Student Check-In
Mood rating (1–10)

Day rating (Very Good → Very Bad)

Sleep hours + sleep time

Loneliness (yes/no)

Last CA / exam score (%)

Emotion (Hinglish prompt) + optional reason

2️⃣ Instant Analysis
evaluate_student(data) applies weighted rules

Adds rule-based points

Collects human-readable reasons

Classifies risk level

Saves to students.json

3️⃣ Action
Risk Level	Response
🔴 HIGH	Support message + helpline + admin alert
🟡 MODERATE	Gentle advice + admin alert
🟢 OK	Positive reinforcement
Admins can review all records via a password-protected dashboard.

🧮 Scoring Logic
Signal	Condition	Points
Mood	≤ 3	+2
Mood	4–5	+1
Day Rating	Bad / Very Bad	+1
CA Score	< 40%	+2
CA Score	40–59%	+1
Sleep	< 5 hours	+1
Loneliness	Yes	+1
Emotion	Sad/Angry/Anxious/Tired/Lonely	+1
Risk Classification:

score >= 4 → 🔴 HIGH_CONCERN

score >= 2 → 🟡 MODERATE_CONCERN

score < 2 → 🟢 OK

✨ Features
What's Already Strong
✅ Input validation loops (no crashes on bad input)

✅ Explainable risk reasons

✅ Separate student / admin flows

✅ Persistent local records (students.json)

✅ Alert logging (admin_alerts.log)

✅ Hinglish-friendly emotion prompt for accessibility

✅ Optional free-text reason (skip with Enter)

✅ Bilingual-ready design

Next Engineering Upgrades
🔐 Encrypt local data + role-based admin access

🕵️ True anonymous mode (when institution permits)

🛠️ Counselor-configurable rules + audit trail

📊 Dashboard UI / Mobile client / ERP integration

🧪 Clinical validation before real-world deployment

🛠 Tech Stack
Component	Technology
Language	Python 3.x
Storage	JSON (local, no backend)
Logging	Plain-text .log files
Dependencies	None — pure standard library
Platform	Any OS (Windows / macOS / Linux)
🚀 Installation & Usage
Prerequisites
Python 3.7 or higher

No pip installs required ✅

Run It
bash
# Clone the repository
git clone https://github.com/<your-username>/mindguardians.git
cd mindguardians

# Run the portal
python project.py
Main Menu
text
============================================================
        MENTAL HEALTH CHECK-IN PORTAL
============================================================
   1. Student Check-in
   2. Admin Dashboard
   3. Exit
============================================================
Student Flow
Enter registration number + college name

Answer 8 quick check-in questions

Receive instant risk classification + support message

Admin Flow
Choose option 2

Enter password: CARS (change this before deploying!)

View summary counts, concerning records, and full alert log

📁 File Structure
text
mindguardians/
│
├── project.py              # Main single-file application
├── students.json           # Auto-generated: all check-in records
├── admin_alerts.log        # Auto-generated: alerts for concerning cases
└── README.md               # You are here
Key Functions
Function	Purpose
collect_feedback()	Collects student check-in fields
evaluate_student()	Applies weighted rules + thresholds
save_student_record()	Appends records to students.json
send_alert_to_admin()	Prints + appends to admin_alerts.log
admin_interface()	Shows summaries + concerning records
main_menu()	Routes Student / Admin / Exit
🗺 Roadmap
Phase	Milestone	Description
1. Pilot	LPU + nearby schools	Deploy prototype locally
2. Predict	Validated ML analytics	Layer ML on top of rule-based flags
3. Localize	Punjabi + Hindi + English	Multilingual support
4. Integrate	ERP / Government pathways	Connect to institutional systems
5. Scale	10,000+ institutions	Nationwide rollout
Scalability Principles
🖥️ Works on a normal computer

📴 Offline-first prototype

🌐 Single-file demo → web/mobile architecture

🔗 Can integrate with existing systems

🎯 SDG Alignment
SDG	Goal
SDG 3	Good Health & Well-Being
SDG 4	Quality Education
SDG 10	Reduced Inequalities
Key design principle: Privacy + Explainability + Human Oversight

⚠️ Important Disclaimer
This is a practical prototype — NOT a medical diagnosis.

This tool flags concern; it does not diagnose any condition.

It is designed to bridge students to existing care — earlier, more consistently, and with less friction.

It does not replace counselors or helplines.

If you or someone you know is in crisis, please reach out:

🇮🇳 Helplines

👥 Team
Team MindGuardians • Lovely Professional University • B.Tech CSE — 1st Year

Member	Role
Akshat Gupta	Team Lead & Core Developer
Siddharth Gupta	Developer & Logic Design
Chetna Sharma	Research & Documentation
Roohani	UI/UX & Content
🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page or open a pull request.

Fork the repo

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

🌟 Why This Project Deserves to Move Forward
Pillar	Description
🎯 Real Problem	Targets a genuine student wellbeing gap
🔍 Explainable AI	Every risk point has a visible rule
♿ Accessible	Simple interface; low infrastructure overhead
📈 Scalable	Clear path from prototype to institutional platform
🛡️ Responsible	Flags concern — does not claim to diagnose
🎓 Student-Built	Designed around the realities of student life
<div align="center">
💙 Build the bridge before the gap becomes a crisis.
Team MindGuardians • Lovely Professional University

⭐ If you find this project meaningful, please star the repo!

</div>
