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
    "state_income_tax": {
        "virginia": {
            "2%": {"min": 0, "max": 3000},
            "3%": {"min": 3001, "max": 17000},
            "5%": {"min": 17001, "max": 9000},
            "5.75%": {"min": 9001, "max": "above"}
        }
    },
    "local_taxes": {
        "norfolk_va": {
            "income_tax_rate": 0.01
        }
    },
    "total_tax_rates_example": {
        "federal_rate": "24%",
        "state_rate": "5.75%",
        "local_rate": "1%",
        "total_effective_rate": "30.75%"
    }
}