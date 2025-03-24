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
        "rate": 0.05
    },
    "local_taxes": {
        "sales_tax": {
            "rate": 0.0825,
            "state": 0.029,
            "city": 0.02,
            "county": 0.0025,
            "special_districts": 0.031
        },
        "property_tax": "Varies based on assessed value and district"
    },
    "other_taxes": {
        "local_income_tax": "None",
        "business_taxes": "May apply depending on business"
    }
}