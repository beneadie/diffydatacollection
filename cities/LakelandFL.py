taxdict = {
    "sales_tax": {
        "state": 0.06,
        "local": 0.01,
        "combined": 0.07
    },
    "property_tax": {
        "details": "Varies based on property value and location"
    },
    "federal_income_tax": {
        "brackets_2025": {
            "10%": {"min": 0, "max": 11925, "filing_status": "single"},
            "12%": {"min": 11926, "max": 48475, "filing_status": "single"},
            "22%": {"min": 48476, "max": 103350, "filing_status": "single"},
            "24%": {"min": 103351, "max": 197300, "filing_status": "single"},
            "32%": {"min": 197301, "max": 250525, "filing_status": "single"},
            "35%": {"min": 250526, "max": 626350, "filing_status": "single"},
            "37%": {"min": 626351, "max": "above", "filing_status": "single"},
            "10%": {"min": 0, "max": 23850, "filing_status": "married_jointly"},
            "12%": {"min": 23851, "max": 96950, "filing_status": "married_jointly"},
            "22%": {"min": 96951, "max": 206700, "filing_status": "married_jointly"},
            "24%": {"min": 206701, "max": 394600, "filing_status": "married_jointly"},
            "32%": {"min": 394601, "max": 501050, "filing_status": "married_jointly"},
            "35%": {"min": 501051, "max": 751600, "filing_status": "married_jointly"},
            "37%": {"min": 751601, "max": "above", "filing_status": "married_jointly"}
        }
    },
    "state_income_tax": {
        "rate": 0.0,
        "details": "Florida has no state income tax."
    },
    "other_taxes": {
        "note": "Responsible for federal income taxes and any applicable local taxes."
    }
}