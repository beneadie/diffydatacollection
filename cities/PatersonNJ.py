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
            }
        }
    },
    "new_jersey_state_income_tax": {
        "brackets_2024": {
            "5.525%": {"min": 0, "max": 20000},
            "6.37%": {"min": 20001, "max": 50000},
            "6.925%": {"min": 50001, "max": 70000},
            "7.643%": {"min": 70001, "max": 80000},
            "8.97%": {"min": 80001, "max": 150000},
            "10.75%": {"min": 150001, "max": 250000},
            "11.15%": {"min": 250001, "max": "above"}
        }
    },
    "local_property_taxes": {
        "average_property_tax_rate": 0.0338,
        "additional_taxes": "May include school taxes, municipal taxes, and library taxes"
    },
    "sales_tax": {
        "state": 0.06625
    },
    "other_taxes": {
        "vat": "Not applicable"
    }
}