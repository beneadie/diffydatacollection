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
        "rate_structure": {
            "2.59%": {"max": 53000},
            "2.98%": {"min": 53001, "max": "above"}
        }
    },
    "local_taxes": {
        "sales_tax": {
            "combined": 0.086,
            "state": 0.056,
            "county": 0.007,
            "city": 0.023
        },
        "property_tax": "Varies"
    }
}