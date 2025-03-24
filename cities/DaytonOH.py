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
    "ohio_state_income_tax": {
        "brackets_2023": {
            "2.85%": {"min": 0, "max": 44799},
            "3.23%": {"min": 44800, "max": 89600},
            "3.96%": {"min": 89601, "max": 110650},
            "4.24%": {"min": 110651, "max": 221300},
            "4.41%": {"min": 221301, "max": "above"}
        }
    },
    "local_taxes": {
        "dayton_city_income_tax": 0.0225,
        "montgomery_county_property_tax": "Rates vary based on property value and location",
        "ohio_sales_tax": 0.0575,
        "hamilton_county_sales_tax": "N/A",
        "other_local_taxes": "None explicitly noted beyond city income tax"
    },
    "additional_taxes_for_nurses": {
        "professional_licensing_fees": "Vary based on licensure type and are paid to the Ohio Board of Nursing",
        "business_taxes": "If operating a private practice, additional business taxes may apply"
    }
}