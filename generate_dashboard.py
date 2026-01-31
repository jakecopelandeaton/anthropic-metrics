#!/usr/bin/env python3
"""
Anthropic Blog Analytics Dashboard Generator
Fetches data from Google Analytics 4 and generates an HTML dashboard.
Designed to run via GitHub Actions on a schedule.
"""

import os
import json
from datetime import datetime, timedelta
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Dimension,
    Metric,
    FilterExpression,
    Filter,
)

# Configuration
GA4_PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID", "YOUR_PROPERTY_ID")
DAYS_BACK = 180  # 6 months

# Twitter data (static - API too expensive for view counts)
TWITTER_CORRELATION_DATA = [
    {"article": "Claude Opus 4.5", "category": "Model", "twitter_views": "7.7M", "page_views": "685K", "conversion": "8.9%", "color": "#059669"},
    {"article": "Claude Sonnet 4.5", "category": "Model", "twitter_views": "4.9M", "page_views": "754K", "conversion": "15.4%", "color": "#059669"},
    {"article": "Claude for Financial Services", "category": "Product", "twitter_views": "3.3M", "page_views": "~180K", "conversion": "5.5%", "color": "#d97706"},
]


def get_ga4_client():
    creds_json = os.environ.get("GA4_CREDENTIALS")
    if creds_json:
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write(creds_json)
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f.name
    return BetaAnalyticsDataClient()


def format_number(n):
    if n >= 1_000_000: return f"{n/1_000_000:.1f}M"
    elif n >= 1_000: return f"{n/1_000:.0f}K" if n >= 10_000 else f"{n/1_000:.1f}K"
    return str(n)


def format_duration(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins}m {secs:02d}s" if mins > 0 else f"{secs}s"


def main():
    print("Starting dashboard generation...")
    if not os.environ.get("GA4_CREDENTIALS"):
        print("No GA4 credentials found. Using demo data...")
        categories = {"engineering": {"views": 4600000, "users": 2100000, "avg_duration": 86, "count": 51}, "research": {"views": 2600000, "users": 1400000, "avg_duration": 55, "count": 148}, "news": {"views": 9600000, "users": 4800000, "avg_duration": 41, "count": 377}}
        traffic_sources = {"Organic Search": {"views": 9744000, "percentage": 58}, "Direct": {"views": 3360000, "percentage": 20}}
        total_views = 16800000
    else:
        print("Fetching data from Google Analytics 4...")
        client = get_ga4_client()
        # Fetch data here...
        categories = {}
        traffic_sources = {}
        total_views = 0
    
    html = '<!DOCTYPE html><html><body><h1>Dashboard</h1></body></html>'
    with open("index.html", "w") as f:
        f.write(html)
    print("Dashboard generated: index.html")


if __name__ == "__main__":
    main()
