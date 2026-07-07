import json
import datetime

def generate_dashboard_data():
    # Physis (Body) - Removed sleep/recovery
    physis = {
        "weight_trend": [81.2, 80.9, 81.1, 80.6, 80.5, 80.2, 79.9],
        "kfa_trend": [15.2, 15.1, 15.1, 14.9, 14.8, 14.7, 14.5],
        "workout_consistency": [
            # 4 weeks (28 days) of workout indicators (0 = rest, 1 = cardio, 2 = strength, 3 = intense hybrid)
            2, 0, 3, 0, 2, 1, 0,
            2, 0, 3, 1, 2, 0, 0,
            3, 0, 2, 0, 3, 1, 0,
            2, 1, 3, 0, 2, 0, 1
        ]
    }

    # Finanzen (Finance)
    finanzen = {
        "networth": 128450.00,
        "networth_delta_24h": 342.50,
        "portfolio": [
            {"asset": "BTC", "amount": 0.72, "value": 62300.00, "roi": 142.3},
            {"asset": "ETH", "amount": 5.4, "value": 3150.00, "roi": 88.5},
            {"asset": "VOO ETF", "amount": 120.0, "value": 485.00, "roi": 19.1},
            {"asset": "Cash (CHF)", "amount": 12845.00, "value": 1.00, "roi": 0.0}
        ],
        "news_feed": [
            {"ticker": "BTC", "headline": "Macro liquidity indicators signaling potential accumulation breakout.", "time": "1h ago", "sentiment": "bullish"},
            {"ticker": "VOO", "headline": "S&P 500 futures experience volume accumulation above key moving averages.", "time": "3h ago", "sentiment": "bullish"},
            {"ticker": "ETH", "headline": "Ethereum gas fees stabilize at lowest multi-month averages, boosting L2 throughput.", "time": "5h ago", "sentiment": "neutral"}
        ],
        "todos": [
            {"task": "Prepare and optimize documents for tax deduction filings", "done": False},
            {"task": "Automate monthly Swissquote asset accumulation sweeper", "done": True}
        ]
    }

    # Ausbildung (Education - Data Science & Informatics) - Unified Academic Hub
    ausbildung = {
        "gpa": 5.4, # Swiss grading system (1-6, 6 is best)
        "ects_earned": 124,
        "ects_required": 180,
        "calendar": [
            {"event": "Advanced Machine Learning Exam", "date": "2026-07-16", "type": "Exam", "priority": "critical"},
            {"event": "Neural Networks Term Paper Submission", "date": "2026-07-22", "type": "Submission", "priority": "high"},
            {"event": "Distributed Systems Lab Final", "date": "2026-07-30", "type": "Exam", "priority": "high"},
            {"event": "Informatics Bachelor Colloquium Presentation", "date": "2026-08-12", "type": "Presentation", "priority": "critical"}
        ],
        "backlog": [
            {"id": "a1", "task": "Implement Transformer self-attention block in PyTorch", "weight": 5, "tag": "ML", "done": False},
            {"id": "a2", "task": "Review Raft consensus protocol notes for Distributed Systems", "weight": 3, "tag": "Sys", "done": True},
            {"id": "a3", "task": "Draft abstract for Bachelor thesis on decentralized deep learning", "weight": 8, "tag": "Thesis", "done": False},
            {"id": "a4", "task": "Complete weekly exercises for Data Engineering pipelines", "weight": 2, "tag": "DE", "done": False}
        ]
    }

    # Utilities & Motivation - Birthdate set to 06.12.2001, removed work backlog
    utilities = {
        "birthdate": "2001-12-06",
        "location": "Bern/Toffen, CH"
    }

    dashboard_data = {
        "generated_at": datetime.datetime.now().isoformat(),
        "physis": physis,
        "finanzen": finanzen,
        "ausbildung": ausbildung,
        "utilities": utilities
    }

    return dashboard_data

if __name__ == "__main__":
    data = generate_dashboard_data()
    with open("/dashboard-yannis/dashboard_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Successfully generated clean /dashboard-yannis/dashboard_data.json without sleep and work backlog structures.")
