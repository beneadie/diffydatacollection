taxdict = {
    "sales_tax": {
        "state": 0.04,
        "local": 0.02,
        "combined": 0.06
    },
    "property_tax": {
        "details": "Vary based on assessed property value and location within Ann Arbor"
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
             "married_filing_jointly":{
                "10%": {"min": 0, "max": 23850},
                "12%": {"min": 23851, "max": 96950},
                "22%": {"min": 96951, "max": 206700},
                "24%": {"min": 206701, "max": 394600},
                "32%": {"min": 394601, "max": 501050},
                "35%": {"min": 501051, "max": 751600},
                "37%": {"min": 751601, "max": "above"}
            },

        }
    },
    "state_income_tax": {
        "rate": 0.0425
    },
    "local_income_tax": {
        "city_ann_arbor": 0.01
    },
    "other_taxes": {
        "federal_medicare_tax": "1.45%"
    }
}