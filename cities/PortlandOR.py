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
    "state_income_tax": {
        "oregon_2024": {
            "5%": {"min": 0, "max": 3750},
            "7%": {"min": 3751, "max": 9000},
            "9%": {"min": 9001, "max": 12000},
            "9.9%": {"min": 12001, "max": "above"}
        }
    },
    "local_taxes": {
        "portland_arts_tax": "2.2% of taxable income",
        "trimet_self_employment_tax": "0.007147",
        "multnomah_county_tax": "Varies based on property value"
    },
    "sales_tax": {
        "state": "None",
        "local": "May apply in certain areas"
    },
    "property_tax": "Varies based on property value and location"
}