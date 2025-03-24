taxdict = {
    "federal_income_tax": {
        "brackets_2025_single": {
            "10%": {"min": 0, "max": 11925},
            "12%": {"min": 11926, "max": 48475},
            "22%": {"min": 48476, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250525},
            "35%": {"min": 250526, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
        },
        "brackets_2025_married_jointly": {
            "10%": {"min": 0, "max": 23850},
            "12%": {"min": 23851, "max": 96950},
            "22%": {"min": 96951, "max": 206700},
            "24%": {"min": 206701, "max": 394600},
            "32%": {"min": 394601, "max": 501050},
            "35%": {"min": 501051, "max": 751600},
            "37%": {"min": 751601, "max": "above"}
        }
    },
    "state_income_tax": {
        "brackets_2023_single": {
            "0.36%": {"min": 0, "max": 1743},
            "0.48%": {"min": 1744, "max": 3487},
            "2.25%": {"min": 3488, "max": 6975},
            "4.14%": {"min": 6976, "max": 13950},
            "5.63%": {"min": 13951, "max": 20950},
            "5.98%": {"min": 20951, "max": "above"}
        },
        "brackets_2023_married_jointly": {
            "0.36%": {"min": 0, "max": 3487},
            "0.48%": {"min": 3488, "max": 6975},
            "2.25%": {"min": 6976, "max": 13950},
            "4.14%": {"min": 13951, "max": 27900},
            "5.63%": {"min": 27901, "max": 41900},
            "5.98%": {"min": 41901, "max": "above"}
        }
    },
    "local_taxes": {
        "sales_tax": {
            "state": 0.06,
            "county": 0.01,
            "combined": 0.07
        },
        "property_tax": "Varies based on assessed property value and location"
    },
    "other_taxes": {
        "social_security_tax": "6.2% up to $147,000 wage base in 2023",
        "medicare_tax": "1.45%"
    }
}