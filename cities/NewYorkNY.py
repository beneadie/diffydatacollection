taxdict = {
    "sales_tax": {
        "state": 0.06,
        "county": 0.02,
        "city": 0.0,
        "combined": 0.08
    },
    "property_tax": {
        "city": 0.6045,
        "county": 0.00,
        "interest_rate": "1.5% per month on unpaid balance"
    },
    "federal_income_tax": {
        "brackets_2024": {
               "10%": {"min": 0, "max": 11600},
               "12%": {"min": 11600, "max": 47150},
               "22%": {"min": 47150, "max": 100525},
               "24%": {"min": 100525, "max": 191950},
               "32%": {"min": 191950, "max": 243725},
               "35%": {"min": 243725, "max": 609350},
               "37%": {"min": 609350, "max": "above"}
          }
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees",
        "medicare_tax": "1.45%"
    },
    "nurse_specific_taxes": {
        "travel_nursing_taxes": "Not Specifically Mentioned"
    }
}