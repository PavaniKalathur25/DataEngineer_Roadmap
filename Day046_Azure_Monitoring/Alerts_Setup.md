---

#### 📘 `alerts_setup.md`
```markdown
# 🚨 Creating Alerts & Dashboards

## Step 1 – Create an Alert Rule
1. Go to **Azure Monitor → Alerts → New Alert Rule**  
2. Choose target resource (e.g., Data Factory).  
3. Define condition (e.g., pipeline failures > 0).  
4. Add action group (email or Teams notification).  
5. Save the alert.

## Step 2 – Build a Dashboard
1. Open **Azure Portal → Dashboard → New**.  
2. Add Log Analytics queries as charts.  
3. Pin Metrics and Alerts for ADF, Synapse, ADLS.

## Step 3 – Automate with Logic Apps
Trigger an email or Slack notification when alert fires.
