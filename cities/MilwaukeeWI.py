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
            "married_jointly": {
                "10%": {"min": 0, "max": 23850},
                "12%": {"min": 23851, "max": 96950},
                "22%": {"min": 96951, "max": 206700},
                "24%": {"min": 206701, "max": 394600},
                "32%": {"min": 394601, "max": 501050},
                "35%": {"min": 501051, "max": 751600},
                "37%": {"min": 751601, "max": "above"}
            },
            "head_of_household": {
                "10%": {"min": 0, "max": 17000},
                "12%": {"min": 17001, "max": 64850},
                "22%": {"min": 64851, "max": 103350},
                "24%": {"min": 103351, "max": 197300},
                "32%": {"min": 197301, "max": 250500},
                "35%": {"min": 250501, "max": 626350},
                "37%": {"min": 626351, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "wisconsin": {
            "brackets": {
                "4.00%": {"min": 0, "max": 12400},
                "5.84%": {"min": 12401, "max": 31900},
                "7.65%": {"min": 31901, "max": "above"}
            }
        }
    },
    "local_taxes": {
        "sales_tax": {
            "milwaukee_county": 0.005,
            "wisconsin_state": 0.05
        },
        "property_tax": {
            "milwaukee_city": "varies"
        }
    },
    "other_taxes": {
        "wisconsin_homestead_credit": "available",
        "wisconsin_earned_income_tax_credit": "available"
    }
}