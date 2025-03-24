taxdict = {
    "sales_tax": {
        "state": 0.0725,
        "local": 0.015,
        "combined": 0.0875
    },
    "property_tax": {
        "rate": "0.8% - 1.2% of assessed value annually"
    },
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
        "brackets": {
            "9.3%": {"min": 0, "max": 9350},
            "10.3%": {"min": 9351, "max": 22733},
            "11.3%": {"min": 22734, "max": 34392},
            "12.3%": {"min": 34393, "max": 46359},
            "13.3%": {"min": 46360, "max": 56085},
            "13.3% + 1% surtax over $1 million": {"min": 56085, "max": "above"}
        }
    },
    "other_taxes": {
        "miscellaneous_taxes": "May include taxes on specific goods like gasoline, tobacco, and alcohol"
    }
}