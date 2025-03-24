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
        "rate": 0.0307
    },
    "local_taxes": {
        "city_wage_tax": 0.01,
        "property_tax_allegheny_county": "Varies based on property value, around 2.16% of property value",
        "sales_tax": 0.07
    },
    "other_taxes": {
        "medicare_tax": "1.45% (may be subject to additional 0.9% on earnings above $200,000)",
        "social_security_tax": "6.2% (on earnings up to $137,700 for 2023)"
    }
}