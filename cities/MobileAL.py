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
        "alabama": {
            "single": {
                "2%": {"min": 0, "max": 997},
                "4%": {"min": 998, "max": 6000},
                "5%": {"min": 6001, "max": "above"}
            },
            "married_jointly": {
                "2%": {"min": 0, "max": 1997},
                "4%": {"min": 1998, "max": 12000},
                "5%": {"min": 12001, "max": "above"}
            }
        }
    },
    "local_income_tax": {
        "mobile_city": 0.03,
        "mobile_county": 0.01
    },
    "sales_tax": {
        "state": 0.04,
        "city": 0.03,
        "county": 0.01,
        "total": 0.08
    },
    "property_tax": {
        "details": "Varies based on assessed property value and location within Mobile."
    },
    "other_taxes": {
        "value_added_tax": "Not applicable in the US",
        "miscellaneous_local_fees": "May apply depending on specific services used"
    }
}