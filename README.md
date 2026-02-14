# Apache Superset: From Clone to Database Connection

This guide provides step-by-step instructions to set up Apache Superset and connect it to your analytics database.

## Prerequisites
- Python 3.9+
- Node.js 16+
- npm 7+

---

## Step 1: Clone the Repository
```bash
git clone https://github.com/shariqfalconsystem/dronaAIM-superset.git
cd dronaAIM-superset
```
*(Note: If you are already inside the directory, skip to Step 2)*

## Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies
```bash
pip install -r superset/requirements/base.txt
pip install -e superset/
```

## Step 4: Initialize Superset Metadata Database
```bash
export FLASK_APP=superset
superset db upgrade
```

## Step 5: Create Admin User
```bash
superset fab create-admin
```

## Step 6: Initialize Superset
```bash
superset init
```

## Step 7: Build Frontend
```bash
cd superset/superset-frontend
npm install
npm run build
cd ../..
```

## Step 8: Run Superset Server
```bash
superset run -p 8088 --with-threads --reload --debugger
```

## Step 9: Access Superset UI
Open your browser and navigate to: [http://localhost:8088](http://localhost:8088)

## Step 10: Connect Your Analytics Database
1. Go to **Settings** → **Database Connections**.
2. Click **+ Database**.
3. Choose your database type and enter the connection URI.

**Example PostgreSQL URI:**
```text
postgresql+psycopg2://user:password@host:5432/ads_db
```

---

## Final Outcome
Superset is now connected to your database and ready for chart and dashboard creation!
