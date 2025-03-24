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
            "married_filing_jointly": {
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
    "north_dakota_state_income_tax": {
        "brackets_2023": {
            "2.04%": {"min": 0, "max": 44700},
            "4.22%": {"min": 44701, "max": 89400},
            "5.35%": {"min": 89401, "max": 178700},
            "5.99%": {"min": 178701, "max": "above"}
        }
    },
    "local_taxes": {
        "sales_tax": {
            "combined": 0.07
        },
        "property_tax": "Varies based on assessed property value and location"
    },
    "other_taxes": "payroll taxes and other specific industry taxes may apply"
}