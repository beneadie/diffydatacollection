taxdict = {
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
            "married_jointly":{
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
    "state_income_tax": {
        "new_jersey": {
            "brackets": {
                "5.525%": {"min": 0, "max": 20000},
                "6.37%": {"min": 20001, "max": 50000},
                "6.925%": {"min": 50001, "max": 70000},
                "7.643%": {"min": 70001, "max": 80000},
                "8.97%": {"min": 80001, "max": 500000},
                "10.75%": {"min": 500001, "max": "above"}
            }
        }
    },
    "local_taxes": {
        "property_tax": {
            "jersey_city": 0.0131
        },
        "sales_tax": {
            "combined": 0.06625,
            "state_rate": 0.033125,
            "local_rate": 0.033125
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees (12.4% for self-employed), up to $142,800 in earnings (2023)",
        "medicare_tax": "1.45% for employees (2.9% for self-employed), no income limit"
    }
}