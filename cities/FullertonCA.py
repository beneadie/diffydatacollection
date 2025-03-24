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
        "brackets_2023_single": {
            "9.3%": {"min": 0, "max": 9350},
            "10.3%": {"min": 9351, "max": 22733},
            "11.3%": {"min": 22734, "max": 34392},
            "12.3%": {"min": 34393, "max": 48807},
            "13.3%": {"min": 48808, "max": "above"}
        },
        "brackets_2023_married_jointly": {
            "9.3%": {"min": 0, "max": 18700},
            "10.3%": {"min": 18701, "max": 45467},
            "11.3%": {"min": 45468, "max": 68784},
            "12.3%": {"min": 68785, "max": "above"}
        }
    },
    "local_taxes": {
        "sales_tax": 0.0875,
        "property_tax": "around 1.25% of assessed value"
    },
    "other_taxes": {
        "fica_tax": 0.0765
    }
}