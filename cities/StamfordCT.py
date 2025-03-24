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
        "rate": "3% - 7% based on income level",
        "brackets_2023": {
            "3%": {"min": 0, "max": 10000},
            "5%": {"min": 10001, "max": 50000},
            "5.5%": {"min": 50001, "max": 100000},
            "6%": {"min": 100001, "max": 200000},
            "6.5%": {"min": 200001, "max": 250000},
            "7%": {"min": 250001, "max": "above"}
        }
    },
    "local_property_tax": {
        "city_stamford": 0.0225,
        "example": "For a home assessed at $500,000, annual property tax would be $11,250"
    },
    "sales_tax": {
        "state": 0.0635,
        "luxury_goods": "7.35% total on items like jewelry and clothing over $100"
    },
    "other_taxes": {
        "payroll_taxes": {
            "social_security": "6.2% employer, 6.2% employee",
            "medicare": "1.45% employer, 1.45% employee"
        },
        "business_taxes": "Vary based on business type and income level"
    }
}