# Anthropic Blog Analytics Dashboard

Auto-updating dashboard that pulls data from Google Analytics 4 and deploys to GitHub Pages.

**Live URL:** `https://jakecopelandeaton.github.io/anthropic-metrics/`

## How It Works

1. **GitHub Actions** runs daily at 6 AM UTC
2. **Python script** fetches latest data from GA4 API
3. **Generates** a new `index.html` with current stats
4. **Commits** changes and deploys to GitHub Pages

## Setup Instructions

### 1. Create a Google Cloud Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use existing)
3. Enable the **Google Analytics Data API**
4. Go to **IAM & Admin → Service Accounts**
5. Create a service account
6. Download the JSON key file

### 2. Add Service Account to GA4

1. Go to [Google Analytics](https://analytics.google.com/)
2. Navigate to **Admin → Property → Property Access Management**
3. Add the service account email
4. Grant **Viewer** role

### 3. Get Your GA4 Property ID

1. In GA4, go to **Admin → Property Settings**
2. Copy the **Property ID** (numeric, e.g., `123456789`)

### 4. Add GitHub Secrets

In your GitHub repo, go to **Settings → Secrets and variables → Actions** and add:

| Secret Name | Value |
|-------------|-------|
| `GA4_PROPERTY_ID` | Your GA4 property ID |
| `GA4_CREDENTIALS` | The entire contents of the JSON key file |

### 5. Enable GitHub Pages

1. Go to **Settings → Pages**
2. Under "Build and deployment", select **GitHub Actions**

### 6. Run It!

1. Go to **Actions** tab
2. Select "Update Dashboard" workflow
3. Click **Run workflow** to test

## Notes

- **Twitter data** is a static snapshot — Twitter's API doesn't provide view counts on affordable tiers
- Dashboard updates daily at 6 AM UTC
- You can trigger manual updates via the Actions tab
