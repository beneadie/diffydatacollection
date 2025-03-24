taxdict = {
    "sales_tax": {
        "state": 0.06,
        "county": 0.01,
        "city": 0.0025,
        "transportation": 0.01,
        "combined": 0.0825
    },
    "property_tax": {
        "effective_rate": "0.008 to 0.0125 (of assessed value)"
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
        "brackets_2023": {
            "9.3%": {"max": 53099},
            "10.3%": {"min": 53100, "max": 266745},
            "11.3%": {"min": 266746, "max": 322499},
            "12.3%": {"min": 322500, "max": 407499},
            "13.3%": {"min": 407500, "max": "above"}
        }
    },
    "local_income_tax": "None",
    "other_taxes": {
        "value_added_tax": "Not Applicable"
    }
}