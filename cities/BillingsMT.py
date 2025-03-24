taxdict = {
    "sales_tax": {
        "state": 0.0,
        "local": 0.03,
        "combined": 0.03
    },
    "property_tax": {
        "note": "Varies based on assessed property value and location"
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
            "married_filing_jointly": {
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
        "brackets": {
            "1%": {"min": 0, "max": 2900},
            "2%": {"min": 2901, "max": 5100},
            "3%": {"min": 5101, "max": 8300},
            "4%": {"min": 8301, "max": 11300},
            "5%": {"min": 11301, "max": 14600},
            "6%": {"min": 14601, "max": 18400},
            "6.9%": {"min": 18401, "max": "above"}
        }
    },
    "other_taxes": {
        "vat": "Not applicable",
        "miscellaneous_taxes": "May include taxes on specific goods or services"
    }
}