taxdict = {
    "sales_tax": {
        "state": 0.043,
        "local": 0.01,
        "combined": 0.053
    },
    "property_taxes": {
        "real_estate_tax_rate": 0.0093,
        "personal_property_tax_rate": 0.0375
    },
    "income_tax": {
        "federal_income_tax_2025": {
            "single": {
                "10%": {"min": 0, "max": 11925},
                "12%": {"min": 11926, "max": 48475},
                "22%": {"min": 48476, "max": 103350},
                "24%": {"min": 103351, "max": 197300},
                "32%": {"min": 197301, "max": 250525},
                "35%": {"min": 250526, "max": 626350},
                "37%": {"min": 626351, "max": "above"}
            },
             "married_filing_jointly":{
                "10%": {"min": 0, "max": 23850},
                "12%": {"min": 23851, "max": 96950},
                "22%": {"min": 96951, "max": 206700},
                "24%": {"min": 206701, "max": 394600},
                "32%": {"min": 394601, "max": 501050},
                "35%": {"min": 501051, "max": 751600},
                "37%": {"min": 751601, "max": "above"}
            }
        },
        "state_income_tax": 0.0575,
        "local_income_tax": 0.01
    },
    "other_taxes": {
        "vehicle_license_fee": 25,
        "vehicle_registration_fee": 40.75
    }
}