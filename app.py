from flask import Flask, render_template

app = Flask(__name__)

# Stripe Compliance Data: Centralized Policy Content
LEGAL_POLICIES = {
    "privacy": {
        "title": "Privacy Policy",
        "last_updated": "September 2026",
        "content": "Jarboe Digital LLC operates the MarketPulse AI, LeaseShield AI, and AgentFlow CRM platforms. This policy outlines how we collect, use, and protect your personal data. We implement industry-standard encryption protocols (SSL/TLS) across all cloud application containers to secure your credentials and transaction logs. We do not sell, trade, or rent your personal information to third parties."
    },
    "terms": {
        "title": "Terms of Service",
        "last_updated": "September 2026",
        "content": "By accessing the software, e-books, or managed concierge report services provided by Jarboe Digital LLC, you agree to comply with our usage terms. Multi-tier software applications are billed on a recurring subscription basis or metered usage credit matrix. Commercial resale, reverse-engineering, or unauthorized credential sharing of individual user account sessions is strictly prohibited under solo-license tiers."
    },
    "refunds": {
        "title": "Refund & Cancellation Policy",
        "last_updated": "September 2026",
        "content": "Digital product sales (including downloadable e-books) and completed custom 'Done-For-You' concierge document analysis reports are final and non-refundable upon delivery. Monthly software-as-a-service (SaaS) subscription tiers can be canceled at any time directly through your account dashboard settings. Upon cancellation, your payment loop will terminate, and access will remain active until the end of your current billing cycle."
    }
}

@app.route("/")
def home():
    """Renders the master corporate studio showcase page."""
    # We pass the corporate data dictionary straight into Jinja2
    return render_template("index.html", policies=LEGAL_POLICIES)

if __name__ == "__main__":
    # Local development server execution loop
    app.run(host="127.0.0.1", port=5000, debug=True)
