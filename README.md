🚀 PulseBoard API

PulseBoard API is a backend system built using Django and Django REST Framework that allows users to share daily work updates, track progress, and collaborate within teams.

The platform focuses on activity tracking rather than task management, helping teams stay aligned through a centralized update feed.

🎯 Features
🔐 Authentication
JWT-based authentication
User registration & login
Secure API access using access tokens
🧑‍💻 Daily Updates
Create and manage daily work updates
Track progress using status:
PLANNED
IN_PROGRESS
COMPLETED
BLOCKED
👥 Team Collaboration
Create and manage teams
Add members to teams
Associate updates with teams
💬 Interaction System
Comment on updates
React (like) to updates
📰 Activity Feed
Centralized feed for updates
Sorted by latest activity
🔎 Filtering
Filter updates by status
⚙️ Additional Features
Pagination support
Clean modular architecture
Secure endpoints with authentication
🧱 Tech Stack
Backend: Django, Django REST Framework
Authentication: JWT (SimpleJWT)
Database: PostgreSQL / CockroachDB
Tools: Git, Postman
📁 Project Structure
pulseboard-django-backend/
│
├── accounts/         # Authentication (JWT, register, login)
├── users/            # User profile
├── updates/          # Daily updates (core feature)
├── teams/            # Team management
├── comments/         # Comments system
├── reactions/        # Likes / reactions
├── activity_logs/    # Activity tracking
│
├── core/             # Main Django project
├── manage.py
└── requirements.txt
⚙️ Setup Instructions
1️⃣ Clone the repository
git clone <your-repo-url>
cd pulseboard-django-backend
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run migrations
python manage.py migrate
5️⃣ Start server
python manage.py runserver