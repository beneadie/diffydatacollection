taxdict = {
    "sales_tax": {
        "state": 0.0,
        "local": 0.0,
        "combined": 0.0
    },
    "property_tax": {
        "notes": "Varies based on assessed property value (administered by Marion County). Average effective rate is around 0.0085-0.01"
    },
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
    "oregon_state_income_tax": {
        "brackets_2023": {
            "5%": {"min": 0, "max": 3750},
            "7%": {"min": 3751, "max": 9000},
            "9%": {"min": 9001, "max": 12000},
            "9.9%": {"min": 12001, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2%",
        "medicare_tax": "1.45%"
    }
}