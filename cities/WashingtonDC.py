taxdict = {
    "sales_tax": {
        "rate": 0.0575
    },
    "property_tax": {
        "rate": 0.0056
    },
    "federal_income_tax": {
        "brackets_2025": {
            "single": {
                "10%": {"min": 0, "max": 11925},
                "12%": {"min": 11926, "max": 48475},
                "22%": {"min": 48476, "max": 103350},
                "24%": {"min": 103351, "max": 197300},
                "32%": {"min": 197301, "max": 250525},
                "35%": {"min": 250526, "max": 626350},
                "37%": {"min": 626351, "max": "above"}
            },
            "married_filing_jointly": {
                "10%": {"min": 0, "max": 23850},
                "12%": {"min": 23851, "max": 96950},
                "22%": {"min": 96951, "max": 206700},
                "24%": {"min": 206701, "max": 394600},
                "32%": {"min": 394601, "max": 501050},
                "35%": {"min": 501051, "max": 751600},
                "37%": {"min": 751601, "max": "above"}
            }
        }
    },
    "dc_income_tax": {
        "brackets_2023": {
            "single": {
                "4%": {"min": 0, "max": 10000},
                "6%": {"min": 10001, "max": 40000},
                "7%": {"min": 40001, "max": 60000},
                "8.25%": {"min": 60001, "max": 180000},
                "8.95%": {"min": 180001, "max": "above"}
            },
            "married_filing_jointly": {
                "4%": {"min": 0, "max": 20000},
                "6%": {"min": 20001, "max": 60000},
                "7%": {"min": 60001, "max": 100000},
                "8.25%": {"min": 100001, "max": 350000},
                "8.95%": {"min": 350001, "max": "above"}
            }
        }
    },
    "other_taxes": {
        "vat": "no vat in the united states"
    }
}