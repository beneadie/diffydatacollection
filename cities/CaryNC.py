taxdict = {
    "federal_income_tax": {
        "single_2023": {
            "10%": {"min": 0, "max": 11000},
            "12%": {"min": 11001, "max": 44725},
            "22%": {"min": 44726, "max": 95375},
            "24%": {"min": 95376, "max": 182100},
            "32%": {"min": 182101, "max": 231250},
            "35%": {"min": 231251, "max": 578125},
            "37%": {"min": 578126, "max": "above"}
        },
        "married_jointly_2023": {
            "10%": {"min": 0, "max": 22000},
            "12%": {"min": 22001, "max": 89450},
            "22%": {"min": 89451, "max": 190750},
            "24%": {"min": 190751, "max": 364200},
            "32%": {"min": 364201, "max": 462500},
            "35%": {"min": 462501, "max": 693750},
            "37%": {"min": 693751, "max": "above"}
        },
        "brackets_2025": {
            "10%": {"min": 0, "max": 11925},
            "12%": {"min": 11926, "max": 48475},
            "22%": {"min": 48476, "max": 103350},
            "24%": {"min": 103351, "max": 197300},
            "32%": {"min": 197301, "max": 250525},
            "35%": {"min": 250526, "max": 626350},
            "37%": {"min": 626351, "max": "above"}
        }
    },
    "state_income_tax": {
        "north_carolina": 0.0499
    },
    "local_taxes": {
        "property_tax": {
            "wake_county": "0.0072 - 0.0085",
            "cary_city": 0.00305
        },
        "sales_tax": {
            "combined": 0.0725,
            "state": 0.0475,
            "local": 0.025
        }
    },
    "other_taxes": {
        "federal_payroll_tax": {
            "social_security": "6.2% (capped at $8,537.40)",
            "medicare": "1.45%"
        },
        "value_added_tax": "Not applicable"
    }
}