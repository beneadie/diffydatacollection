taxdict = {
    "federal_income_tax": {
        "brackets_2023": {
            "single": {
                "10%": {"min": 0, "max": 11000},
                "12%": {"min": 11001, "max": 44725},
                "22%": {"min": 44726, "max": 95375},
                "24%": {"min": 95376, "max": 182100},
                "32%": {"min": 182101, "max": 231250},
                "35%": {"min": 231251, "max": 578125},
                "37%": {"min": 578126, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 22000},
                "12%": {"min": 22001, "max": 89450},
                "22%": {"min": 89451, "max": 190750},
                "24%": {"min": 190751, "max": 364200},
                "32%": {"min": 364201, "max": 462500},
                "35%": {"min": 462501, "max": 693750},
                "37%": {"min": 693751, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "tennessee": "no state income tax, but has a Hall Income Tax of 1% on certain investments"
    },
    "local_taxes": {
        "sales_tax": {
            "combined": 0.0955,
            "state_rate": 0.04,
            "local_rate": 0.0555
        },
        "property_tax": "1.19% to 1.35% of the assessed value of the property"
    },
    "other_taxes": {
        "social_security_tax": "6.2%",
        "medicare_tax": "1.45%"
    },
    "federal_tax_2025": {
        "brackets_single": {
            "10%": {"min": 0, "max": 11925},
            "12%": {"min": 11926, "max": 48475},
            "22%": {"min": 48476, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250525},
            "35%": {"min": 250526, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
        },
        "brackets_married_jointly": {
            "10%": {"min": 0, "max": 23850},
            "12%": {"min": 23851, "max": 96950},
            "22%": {"min": 96951, "max": 206700},
            "24%": {"min": 206701, "max": 394600},
            "32%": {"min": 394601, "max": 501050},
            "35%": {"min": 501051, "max": 751600},
            "37%": {"min": 751601, "max": "above"}
        },
         "brackets_head_of_household": {
            "10%": {"min": 0, "max": 17000},
            "12%": {"min": 17001, "max": 64850},
            "22%": {"min": 64851, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250500},
            "35%": {"min": 250501, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
        }
    }
}