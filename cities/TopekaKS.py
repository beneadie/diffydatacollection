taxdict = {
    "sales_tax": {
        "state": 0.0415,
        "local": 0.04,
        "combined": 0.0815
    },
    "property_tax": {
        "note": "Varies based on assessed property value and location within Topeka"
    },
    "federal_income_tax": {
        "brackets_2025": {
            "10%": {"min": 0, "max": 11925, "filing_status": ["single", "head of household", "married filing jointly"]},
            "12%": {"min": 11926, "max": 48475, "filing_status": ["single", "head of household", "married filing jointly"]},
            "22%": {"min": 48476, "max": 103350, "filing_status": ["single", "head of household", "married filing jointly"]},
            "24%": {"min": 103351, "max": 197300, "filing_status": ["single", "head of household", "married filing jointly"]},
            "32%": {"min": 197301, "max": 250525, "filing_status": ["single", "head of household", "married filing jointly"]},
            "35%": {"min": 250526, "max": 626350, "filing_status": ["single", "head of household", "married filing jointly"]},
            "37%": {"min": 626351, "max": "above", "filing_status": ["single", "head of household", "married filing jointly"]}
        }
    },
    "kansas_state_income_tax": {
        "brackets_2023": {
            "2.7%": {"min": 0, "max": 2250},
            "5.25%": {"min": 2251, "max": 12500},
            "5.5%": {"min": 12501, "max": 30000},
            "5.7%": {"min": 30001, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees, 12.4% for self-employed",
        "medicare_tax": "1.45% for employees, 2.9% for self-employed"
    }
}