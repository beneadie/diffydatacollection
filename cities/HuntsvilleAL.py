taxdict = {
    "sales_tax": {
        "state": 0.04,
        "local": 0.05,
        "combined": 0.09
    },
    "property_tax": {
        "average_effective_rate": 0.0042
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
          },
        "brackets_2023":{
            "10%": {"single_min": 0, "single_max": 11000, "married_min":0, "married_max": 22000},
            "12%": {"single_min": 11001, "single_max": 44725, "married_min":22001, "married_max": 89450},
            "22%": {"single_min": 44726, "single_max": 95375, "married_min":89451, "married_max": 190750},
            "24%": {"single_min": 95376, "single_max": 182100, "married_min":190751, "married_max": 364200},
            "32%": {"single_min": 182101, "single_max": 231250, "married_min":364201, "married_max": 462500},
            "35%": {"single_min": 231251, "single_max": 578125, "married_min":462501, "married_max": 693750},
            "37%": {"single_min": 578126, "single_max": "above", "married_min":693751, "married_max": "above"}
        }
    },
    "state_income_tax": {
        "brackets": {
            "2%": {"min": 0, "max": 997},
            "4%": {"min": 998, "max": 6000},
            "5%": {"min": 6001, "max": "above"}
        }
    },
    "other_taxes": {
        "social_security_tax": "6.2% (employee portion, up to $142,800 in 2023)",
        "medicare_tax": "1.45%"
    }
}