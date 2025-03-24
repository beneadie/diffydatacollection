taxdict = {
    "federal_income_tax": {
        "brackets_2023_single": {
            "10%": {"min": 0, "max": 11000},
            "12%": {"min": 11001, "max": 44725},
            "22%": {"min": 44726, "max": 95375},
            "24%": {"min": 95376, "max": 182100},
            "32%": {"min": 182101, "max": 231250},
            "35%": {"min": 231251, "max": 578125},
            "37%": {"min": 578126, "max": "above"}
        },
        "brackets_2023_married_jointly": {
            "10%": {"min": 0, "max": 22000},
            "12%": {"min": 22001, "max": 89450},
            "22%": {"min": 89451, "max": 190750},
            "24%": {"min": 190751, "max": 364200},
            "32%": {"min": 364201, "max": 462500},
            "35%": {"min": 462501, "max": 693750},
            "37%": {"min": 693751, "max": "above"}
        }
    },
    "state_income_tax": {
        "rate": "3% to 7% based on income level",
        "brackets_2023": {
            "3%": {"max": 10000},
            "5%": {"min": 10001, "max": 50000},
            "7%": {"min": 50001, "max": "above"}
        }
    },
    "local_property_tax": {
        "city_new_haven": 43.97,
        "units": "mills"
    },
    "sales_and_use_tax": {
        "state": 0.0635,
        "luxury_goods": "1% additional tax on cars over $50,000 and jewelry over $5,000"
    },
    "other_taxes": {
        "local_income_tax": "None beyond state and federal taxes",
        "miscellaneous_taxes": "Various may apply (e.g., on real estate conveyance)"
    }
}