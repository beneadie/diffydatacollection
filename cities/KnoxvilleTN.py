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
        "hall_income_tax": "1% on certain investments"
    },
    "local_taxes": {
        "sales_tax": {
            "rate": 0.0925,
            "details": "includes 7% state rate and 2.25% local rate"
        },
        "property_tax": {
            "effective_rate": 0.0064,
            "details": "Varies depending on assessed value of property"
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% for employees",
        "medicare_tax": "1.45% for employees"
    }
}