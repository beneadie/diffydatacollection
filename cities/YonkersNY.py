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
        "new_york": {
            "brackets_2023": {
                "4%": {"min": 0, "max": 8500},
                "4.5%": {"min": 8501, "max": 11700},
                "5.25%": {"min": 11701, "max": 13900},
                "5.9%": {"min": 13901, "max": 80650},
                "5.97%": {"min": 80651, "max": 215400},
                "6.33%": {"min": 215401, "max": 1077550},
                "6.85%": {"min": 1077551, "max": "above"}
            }
        }
    },
    "local_income_tax": {
        "yonkers": {
            "rate": 0.01
        }
    },
    "sales_tax": {
        "rate": 0.08875
    },
    "property_tax": {
        "note": "Varies based on assessed property value and local assessments"
    },
    "other_taxes": {
        "nurses": "May pay professional licensing fees and other industry-specific taxes."
    }
}