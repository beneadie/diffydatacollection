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
        "tax_rate_oklahoma": {
            "0-2000": 0.0087,
            "2001-5000": 0.0091,
            "5001_and_above": 0.0095
        }
    },
    "local_taxes": {
        "sales_tax": {
            "combined": 0.08417,
            "state": 0.04,
            "city_broken_arrow": 0.02,
            "wagoner_county": 0.02,
            "additional_local": 0.00417
        }
    },
    "other_taxes": {
        "property_tax": "Varies based on assessed property value and location.",
        "value_added_tax": "Not applicable in the United States."
    }
}