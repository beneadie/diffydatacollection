taxdict = {
    "sales_tax": {
        "state": 0.06,
        "county": 0.0025,
        "city": 0.01,
        "additional_local": 0.0225,
        "combined": 0.095
    },
    "property_tax": {
        "rate": "0.008 - 0.012",
        "notes": "Varies based on property value"
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
    "state_income_tax": {
        "brackets": {
            "9.3%": {"min": 0, "max": 9350},
            "10.3%": {"min": 9351, "max": 22733},
            "11.3%": {"min": 22734, "max": 34692},
            "12.3%": {"min": 34693, "max": 46359},
            "13.3%": {"min": 46360, "max": 56085},
            "surtax": {"over": 1000000, "rate": 0.01}
        }
    },
    "other_taxes": {
        "vat": "Not applicable",
        "other_taxes": "May include taxes on specific goods and services such as gasoline, tobacco, and alcohol"
    }
}