taxdict = {
    "sales_tax": {
        "state": 0.0725,
        "county": 0.005,
        "city": 0.005,
        "combined": 0.0825
    },
    "property_tax": {
        "rate_range": "0.008 - 0.012",
        "note": "Varies based on property value"
    },
    "federal_income_tax": {
        "brackets_2025": {
            "10%": {"min": 0, "max": 11925, "filing_status": ["single", "head_of_household"]},
            "12%": {"min": 11926, "max": 48475, "filing_status": ["single", "head_of_household"]},
            "22%": {"min": 48476, "max": 103350, "filing_status": ["single", "head_of_household"]},
            "24%": {"min": 103351, "max": 197300, "filing_status": ["single", "head_of_household"]},
            "32%": {"min": 197301, "max": 250525, "filing_status": ["single", "head_of_household"]},
            "35%": {"min": 250526, "max": 626350, "filing_status": ["single", "head_of_household"]},
            "37%": {"min": 626351, "max": "above", "filing_status": ["single", "head_of_household"]},
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
        "brackets_2024": {
            "9.3%": {"min": 0, "max": 9350, "filing_status": ["single"]},
            "10.3%": {"min": 9351, "max": 21175, "filing_status": ["single"]},
            "11.3%": {"min": 21176, "max": 34000, "filing_status": ["single"]},
            "12.3%": {"min": 34001, "max": 46350, "filing_status": ["single"]},
            "13.3%": {"min": 46351, "max": "above", "filing_status": ["single"]},
            "9.3%": {"min": 0, "max": 18700, "filing_status": ["married_jointly"]},
            "10.3%": {"min": 18701, "max": 42350, "filing_status": ["married_jointly"]},
            "11.3%": {"min": 42351, "max": 68000, "filing_status": ["married_jointly"]},
            "12.3%": {"min": 68001, "max": 92700, "filing_status": ["married_jointly"]},
            "13.3%": {"min": 92701, "max": "above", "filing_status": ["married_jointly"]}
        }
    },
    "other_taxes": {
        "vat": "Not applicable"
    }
}