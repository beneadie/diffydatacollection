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
        "colorado": "5% of taxable income"
    },
    "local_taxes": {
        "sales_tax": {
            "combined": 0.0875,
            "state": 0.029,
            "city_of_aurora": 0.045,
            "special_district": 0.0135
        },
        "property_tax": "Varies based on assessed property value and location within Aurora"
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees (matches the 12.4% total rate)",
        "medicare_tax": "1.45% for employees (matches the 2.9% total rate)"
    }
}