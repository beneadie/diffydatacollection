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
        "brackets_2025_joint": {
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
        "rate": "3% to 7% based on income level",
        "brackets_single": {
            "3%": {"min": 0, "max": 3100},
            "4%": {"min": 3101, "max": 6200},
            "5%": {"min": 6201, "max": 12400},
            "6%": {"min": 12401, "max": 15400},
            "7%": {"min": 15401, "max": "above"}
        },
        "brackets_joint": {
            "3%": {"min": 0, "max": 6200},
            "4%": {"min": 6201, "max": 12400},
            "5%": {"min": 12401, "max": 20800},
            "6%": {"min": 20801, "max": 25600},
            "7%": {"min": 25601, "max": "above"}
        }
    },
    "local_taxes": {
        "sales_tax": {
            "rate": 0.08
        },
        "property_tax": {
            "rate": "around 0.007"
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2%",
        "medicare_tax": "1.45%"
    }
}