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
cd superset
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies
```bash
pip install -r superset/requirements/base.txt
pip install -e superset/
```

## Step 4: Database Configuration
We have configured the main application to use a global PostgreSQL metadata database. 

The connection is already set in `superset/superset_config.py`:
```python
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://testuser:testpass@52.202.251.212:5432/testdb"
```
*(Note: If you change the password on the database server, remember to update it here as well.)*

## Step 5: Initialize Superset Metadata Database
```bash
export FLASK_APP=superset
export SUPERSET_CONFIG_PATH=/home/sabya/work/dronaAIM-superset/superset/superset_config.py
superset db upgrade
```

## Step 6: Create Admin User
```bash
superset fab create-admin
```

## Step 7: Initialize Superset
```bash
superset init
```

## Step 8: Build Frontend
```bash
cd superset/superset-frontend
npm install
npm run build
cd ../..
```

## Step 9: Run Superset Server
Run these commands from the root directory of the project (`/home/sabya/work/dronaAIM-superset`):

```bash
# Ensure you are in the root directory
cd /home/sabya/work/dronaAIM-superset

# Activate the virtual environment
source superset/venv/bin/activate

# Set the configuration path (using the absolute path)
export SUPERSET_CONFIG_PATH=/home/sabya/work/dronaAIM-superset/superset/superset_config.py

# Start the server
superset run -p 8088 --with-threads --reload --debugger
```

## Step 10: Access Superset UI
Open your browser and navigate to: [http://localhost:8088](http://localhost:8088)

## Step 11: Connect Your Analytics Database
1. Go to **Settings** → **Database Connections**.
2. Click **+ Database**.
3. Choose your database type and enter the connection URI.

**Example PostgreSQL URI:**
```text
postgresql+psycopg2://user:password@host:5432/ads_db
```

---

## How to Embed Dashboards
Since you are using a global database, any dashboard you create will have the same ID for all developers.

### Method A: Quick Development (Iframe)
If you just want to see the dashboard inside an iframe quickly (requires you to be logged into Superset in your browser):
1. Use the "Permanent Link" from the dashboard UI.
2. Add `?standalone=true` to the URL.

**The URL for both developers will be:**
`http://localhost:8088/superset/dashboard/p/QoPYEggdL6O/?standalone=true`

### Method B: Production Embedding (SDK)
To embed without requiring a login screen (using the "Guest Token" system we configured):
1. **Pass this ID to the SDK:** `0013ff18-867b-4904-95bf-86b94bf4caf4`
2. **Follow the SDK instructions** using the `GUEST_TOKEN_JWT_SECRET` in `superset_config.py`.

---

## Troubleshooting
### 1. 403 Forbidden Error
If you see a "Forbidden" or 403 error inside the iframe or dashboard:
- **Clear Cookies**: Clear your browser cookies for `localhost`.
- **Incognito Mode**: Always test in an Incognito/Private window to avoid stale session issues.
- **Permission Sync**: If the above fails, run `superset fab edit-user --username <YOUR_USER> --role Admin`.

### 2. Password Reset
If you forget your password or login fails:
```bash
superset fab reset-password --username sabya
```

---

## Final Outcome
Superset is now connected to your global metadata database. Any changes made to dashboards or charts will be shared across all developers. All shared configurations are stored in `superset/superset_config.py`.
