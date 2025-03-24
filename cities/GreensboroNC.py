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
        "north_carolina": 0.0499
    },
    "local_taxes": {
        "sales_tax": {
            "combined": 0.07,
            "state": 0.0475,
            "local": 0.0225
        },
        "property_tax": "Varies based on property value and location within the city"
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees (capped at $8,537.40 for 2023)",
        "medicare_tax": "1.45% for employees (no cap)"
    }
}