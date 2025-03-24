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
    "connecticut_state_income_tax": {
        "rate": "3% - 7% based on income level",
        "brackets_2023": {
            "3%": {"max": 10000},
            "5%": {"min": 10001, "max": 50000},
            "7%": {"min": 50001, "max": "above"}
        }
    },
    "local_property_tax": {
        "real_estate_tax_rate": 0.03973,  # 39.73 mills converted to a decimal
    },
    "sales_tax": {
        "state": 0.0635,
        "luxury_goods": 0.0735
    },
    "other_taxes": {
        "vehicle_property_tax": "Varies",
        "personal_property_tax": "Applies to business equipment and inventory"
    }
}