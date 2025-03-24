taxdict = {
    "federal_income_tax": {
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
    "ohio_state_income_tax": {
        "brackets_2023": {
            "2.85%": {"min": 0, "max": 44725},
            "3.23%": {"min": 44726, "max": 89450},
            "3.96%": {"min": 89451, "max": 110650},
            "4.24%": {"min": 110651, "max": 221300},
            "4.41%": {"min": 221301, "max": "above"}
        }
    },
    "local_taxes": {
        "city_income_tax": 0.021,
    },
    "sales_tax": {
        "state": 0.0575,
    }
}