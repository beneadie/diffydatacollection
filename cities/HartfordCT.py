taxdict = {
    "federal_income_tax": {
        "brackets_2024": {
            "single": {
                "10%": {"min": 0, "max": 11600},
                "12%": {"min": 11601, "max": 47150},
                "22%": {"min": 47151, "max": 100525},
                "24%": {"min": 100526, "max": 191950},
                "32%": {"min": 191951, "max": 243725},
                "35%": {"min": 243726, "max": 609350},
                "37%": {"min": 609351, "max": "above"}
            },
            "married_jointly": {
                "10%": {"min": 0, "max": 23200},
                "12%": {"min": 23201, "max": 94300},
                "22%": {"min": 94301, "max": 191950},
                "24%": {"min": 191951, "max": 383900},
                "32%": {"min": 383901, "max": 487450},
                "35%": {"min": 487451, "max": 731200},
                "37%": {"min": 731201, "max": "above"}
            }
        }
    },
    "state_income_tax": {
        "rate": "3% - 7% (progressive tax system)",
        "brackets": "Vary based on income level and filing status"
    },
    "local_property_tax": {
        "city_hartford": 74.29,
        "unit": "mills (2023 rate)",
        "example": "A $200,000 home would pay approximately $14,858"
    },
    "sales_and_use_tax": {
        "state": 0.0635,
        "local": 0.0
    },
    "other_taxes": {
        "capital_gains_tax": "Federal tax rates apply (15% or 20% depending on income level)",
        "inheritance_and_estate_tax": "Connecticut has both taxes, rates vary based on the size of the estate"
    }
}