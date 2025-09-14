# EcoGuard AI – Environmental Monitoring Agent

**Description:**  
EcoGuard AI is an autonomous agent that monitors air and water quality using sensor data, predicts pollution events, and sends alerts to authorities or communities.

**Features:**
- Real-time environmental data monitoring
- Data visualization using Matplotlib and Seaborn
- Pollution prediction using Prophet
- Automated email alerts for high pollution events

**Tech Stack:** Python, Pandas, Matplotlib, Seaborn, Prophet, LangChain (for agentic behavior), IoT sensors

**Instructions to Run:**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Update your email credentials in `modules/notifier.py`.
3. Run the main script:
   ```bash
   python main.py
   ```
