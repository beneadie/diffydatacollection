list_cities = [
     "New York, NY",
     "Los Angeles, CA",
     "Chicago, IL",
     "Houston, TX",
     "Phoenix, AZ",
     "Philadelphia, PA",
     "San Antonio, TX",
     "San Diego, CA",
     "Dallas, TX",
     "San Jose, CA",
     "Austin, TX",
     "Jacksonville, FL",
     "Fort Worth, TX",
     "Columbus, OH",
     "Charlotte, NC",
     "San Francisco, CA",
     "Seattle, WA",
     "Denver, CO",
     "Oklahoma City, OK",
     "Nashville, TN",
     "El Paso, TX",
     "Washington, DC",
     "Boston, MA",
     "Portland, OR",
     "Las Vegas, NV",
     "Detroit, MI",
     "Memphis, TN",
     "Louisville, KY",
     "Baltimore, MD",
     "Milwaukee, WI",
     "Albuquerque, NM",
     "Tucson, AZ",
     "Fresno, CA",
     "Sacramento, CA",
     "Mesa, AZ",
     "Atlanta, GA",
     "Kansas City, MO",
     "Colorado Springs, CO",
     "Omaha, NE",
     "Raleigh, NC",
     "Miami, FL",
     "Virginia Beach, VA",
     "Long Beach, CA",
     "Oakland, CA",
     "Minneapolis, MN",
     "Tulsa, OK",
     "Tampa, FL",
     "Arlington, TX",
     "Wichita, KS",
     "Aurora, CO",
     "New Orleans, LA",
     "Cleveland, OH",
     "St. Louis, MO",
     "Honolulu, HI",
     "Anaheim, CA",
     "Henderson, NV",
     "Orlando, FL",
     "Lexington, KY",
     "Stockton, CA",
     "Riverside, CA",
     "Corpus Christi, TX",
     "Irvine, CA",
     "Cincinnati, OH",
     "Santa Ana, CA",
     "Newark, NJ",
     "St. Paul, MN",
     "Pittsburgh, PA",
     "Greensboro, NC",
     "Durham, NC",
     "Lincoln, NE",
     "Jersey City, NJ",
     "Plano, TX",
     "Anchorage, AK",
     "North Las Vegas, NV",
     "St. Petersburg, FL",
     "Laredo, TX",
     "Irving, TX",
     "Chesapeake, VA",
     "Glendale, AZ",
     "Winston-Salem, NC",
     "Port St. Lucie, FL",
     "Scottsdale, AZ",
     "Garland, TX",
     "Boise, ID",
     "Norfolk, VA",
     "Spokane, WA",
     "Richmond, VA",
     "Fremont, CA",
     "Huntsville, AL",
     "Frisco, TX",
     "Cape Coral, FL",
     "Santa Clarita, CA",
     "San Bernardino, CA",
     "Tacoma, WA",
     "Hialeah, FL",
     "Baton Rouge, LA",
     "Modesto, CA",
     "Fontana, CA",
     "McKinney, TX",
     "Moreno Valley, CA",
     "Des Moines, IA",
     "Fayetteville, NC",
     "Salt Lake City, UT",
     "Yonkers, NY",
     "Worcester, MA",
     "Rochester, NY",
     "Sioux Falls, SD",
     "Little Rock, AR",
     "Amarillo, TX",
     "Tallahassee, FL",
     "Grand Prairie, TX",
     "Columbus, GA",
     "Augusta, GA",
     "Peoria, AZ",
     "Oxnard, CA",
     "Knoxville, TN",
     "Overland Park, KS",
     "Birmingham, AL",
     "Grand Rapids, MI",
     "Vancouver, WA",
     "Montgomery, AL",
     "Huntington Beach, CA",
     "Providence, RI",
     "Brownsville, TX",
     "Tempe, AZ",
     "Akron, OH",
     "Glendale, CA",
     "Chattanooga, TN",
     "Fort Lauderdale, FL",
     "Newport News, VA",
     "Mobile, AL",
     "Ontario, CA",
     "Clarksville, TN",
     "Cary, NC",
     "Elk Grove, CA",
     "Shreveport, LA",
     "Eugene, OR",
     "Aurora, IL",
     "Salem, OR",
     "Santa Rosa, CA",
     "Rancho Cucamonga, CA",
     "Pembroke Pines, FL",
     "Fort Collins, CO",
     "Springfield, MO",
     "Oceanside, CA",
     "Garden Grove, CA",
     "Lancaster, CA",
     "Murfreesboro, TN",
     "Palmdale, CA",
     "Corona, CA",
     "Killeen, TX",
     "Salinas, CA",
     "Roseville, CA",
     "Denton, TX",
     "Surprise, AZ",
     "Macon, GA",
     "Paterson, NJ",
     "Lakewood, CO",
     "Hayward, CA",
     "Charleston, SC",
     "Alexandria, VA",
     "Hollywood, FL",
     "Springfield, MA",
     "Kansas City, KS",
     "Sunnyvale, CA",
     "Bellevue, WA",
     "Joliet, IL",
     "Naperville, IL",
     "Escondido, CA",
     "Bridgeport, CT",
     "Savannah, GA",
     "Olathe, KS",
     "Mesquite, TX",
     "Pasadena, TX",
     "McAllen, TX",
     "Rockford, IL",
     "Gainesville, FL",
     "Syracuse, NY",
     "Pomona, CA",
     "Visalia, CA",
     "Thornton, CO",
     "Waco, TX",
     "Jackson, MS",
     "Columbia, SC",
     "Lakewood, NJ",
     "Fullerton, CA",
     "Torrance, CA",
     "Victorville, CA",
     "Midland, TX",
     "Orange, CA",
     "Miramar, FL",
     "Hampton, VA",
     "Warren, MI",
     "Stamford, CT",
     "Cedar Rapids, IA",
     "Elizabeth, NJ",
     "Palm Bay, FL",
     "Dayton, OH",
     "New Haven, CT",
     "Coral Springs, FL",
     "Meridian, ID",
     "West Valley City, UT",
     "Pasadena, CA",
     "Lewisville, TX",
     "Kent, WA",
     "Sterling Heights, MI",
     "Fargo, ND",
     "Carrollton, TX",
     "Santa Clara, CA",
     "Round Rock, TX",
     "Norman, OK",
     "Columbia, MO",
     "Abilene, TX",
     "Athens, GA",
     "Pearland, TX",
     "Clovis, CA",
     "Topeka, KS",
     "College Station, TX",
     "Simi Valley, CA",
     "Allentown, PA",
     "West Palm Beach, FL",
     "Thousand Oaks, CA",
     "Vallejo, CA",
     "Wilmington, NC",
     "Rochester, MN",
     "Concord, CA",
     "Lakeland, FL",
     "North Charleston, SC",
     "Lafayette, LA",
     "Arvada, CO",
     "Independence, MO",
     "Billings, MT",
     "Fairfield, CA",
     "Hartford, CT",
     "Ann Arbor, MI",
     "Broken Arrow, OK",
     "Berkeley, CA",
     "Cambridge, MA",
     "Richardson, TX",
     "Antioch, CA",
     "High Point, NC",
     "Clearwater, FL",
     "Pueblo, CO",
     "Pompano Beach, FL",
     "Springfield, IL",
     "Lowell, MA",
     "West Covina, CA",
     "Erie, PA",
     "Centennial, CO",
     "Norwalk, CA",
     "Carlsbad, CA",
     "Burbank, CA",
     "Westminster, CA",
     "Brockton, MA",
     "Visalia, CA",
     "Costa Mesa, CA",
     "Downey, CA",
     "Miami Gardens, FL",
     "El Cajon, CA",
     "San Mateo, CA",
     "Sandy Springs, GA",
     "North Hempstead, NY",
     "Lansing, MI",
     "Daly City, CA",
     "Rialto, CA",
     "El Monte, CA",
     "Elizabeth, NJ",
     "South Bend, IN",
     "Vacaville, CA",
     "West Jordan, UT",
     "Waterbury, CT",
     "Davenport, IA",
     "Roseville, CA",
     "Thornton, CO",
     "Alhambra, CA",
     "Beaumont, TX",
     "Lee's Summit, MO",
     "Allentown, PA",
     "Surprise, AZ",
     "Clarksville, TN",
     "Abilene, TX",
     "Round Rock, TX",
     "Amarillo, TX",
     "North Las Vegas, NV",
     "Lansing, MI",
     "Midland, TX",
     "Palmdale, CA",
     "Springfield, MO",
     "Pasadena, TX",
     "Macon, GA",
     "Pomona, CA",
     "Escondido, CA",
     "Denton, TX",
     "Waco, TX",
     "Joliet, IL",
     "McAllen, TX",
     "Bellevue, WA",
     "Rockford, IL",
     "Carrollton, TX",
     "Grand Prairie, TX",
     "Columbia, SC",
     "Miramar, FL",
     "Chula Vista, CA",
     "Sioux Falls, SD",
     "Port St. Lucie, FL",
     "North Charleston, SC",
     "Naperville, IL",
     "Overland Park, KS",
     "Santa Clarita, CA",
     "Cary, NC"
]


cities_tax = [
     "Thousand Oaks, CA",
     "Vallejo, CA",
     "Wilmington, NC",
     "Rochester, MN",
     "Concord, CA",
     "Lakeland, FL",
     "North Charleston, SC",
     "Lafayette, LA",
     "Arvada, CO",
     "Independence, MO",
     "Billings, MT",
     "Fairfield, CA",
     "Hartford, CT",
     "Ann Arbor, MI",
     "Broken Arrow, OK",
     "Berkeley, CA",
     "Cambridge, MA",
     "Richardson, TX",
     "Antioch, CA",
     "High Point, NC",
     "Clearwater, FL",
     "Pueblo, CO",
     "Pompano Beach, FL",
     "Springfield, IL",
     "Lowell, MA",
     "West Covina, CA",
     "Erie, PA",
     "Centennial, CO",
     "Norwalk, CA",
     "Carlsbad, CA",
     "Burbank, CA",
     "Westminster, CA",
     "Brockton, MA",
     "Visalia, CA",
     "Costa Mesa, CA",
     "Downey, CA",
     "Miami Gardens, FL",
     "El Cajon, CA",
     "San Mateo, CA",
     "Sandy Springs, GA",
     "North Hempstead, NY",
     "Lansing, MI",
     "Daly City, CA",
     "Rialto, CA",
     "El Monte, CA",
     "Elizabeth, NJ",
     "South Bend, IN",
     "Vacaville, CA",
     "West Jordan, UT",
     "Waterbury, CT",
     "Davenport, IA",
     "Roseville, CA",
     "Thornton, CO",
     "Alhambra, CA",
     "Beaumont, TX",
     "Lee's Summit, MO",
     "Allentown, PA",
     "Surprise, AZ",
     "Clarksville, TN",
     "Abilene, TX",
     "Round Rock, TX",
     "Amarillo, TX",
     "North Las Vegas, NV",
     "Lansing, MI",
     "Midland, TX",
     "Palmdale, CA",
     "Springfield, MO",
     "Pasadena, TX",
     "Macon, GA",
     "Pomona, CA",
     "Escondido, CA",
     "Denton, TX",
     "Waco, TX",
     "Joliet, IL",
     "McAllen, TX",
     "Bellevue, WA",
     "Rockford, IL",
     "Carrollton, TX",
     "Grand Prairie, TX",
     "Columbia, SC",
     "Miramar, FL",
     "Chula Vista, CA",
     "Sioux Falls, SD",
     "Port St. Lucie, FL",
     "North Charleston, SC",
     "Naperville, IL",
     "Overland Park, KS",
     "Santa Clarita, CA",
     "Cary, NC"
]


cities_col = [
     "Pasadena, TX",
     "McAllen, TX",
     "Rockford, IL",
     "Gainesville, FL",
     "Syracuse, NY",
     "Pomona, CA",
     "Visalia, CA",
     "Thornton, CO",
     "Waco, TX",
     "Jackson, MS",
     "Columbia, SC",
     "Lakewood, NJ",
     "Fullerton, CA",
     "Torrance, CA",
     "Victorville, CA",
     "Midland, TX",
     "Orange, CA",
     "Miramar, FL",
     "Hampton, VA",
     "Warren, MI",
     "Stamford, CT",
     "Cedar Rapids, IA",
     "Elizabeth, NJ",
     "Palm Bay, FL",
     "Dayton, OH",
     "New Haven, CT",
     "Coral Springs, FL",
     "Meridian, ID",
     "West Valley City, UT",
     "Pasadena, CA",
     "Lewisville, TX",
     "Kent, WA",
     "Sterling Heights, MI",
     "Fargo, ND",
     "Carrollton, TX",
     "Santa Clara, CA",
     "Round Rock, TX",
     "Norman, OK",
     "Columbia, MO",
     "Abilene, TX",
     "Athens, GA",
     "Pearland, TX",
     "Clovis, CA",
     "Topeka, KS",
     "College Station, TX",
     "Simi Valley, CA",
     "Allentown, PA",
     "West Palm Beach, FL",
     "Thousand Oaks, CA",
     "Vallejo, CA",
     "Wilmington, NC",
     "Rochester, MN",
     "Concord, CA",
     "Lakeland, FL",
     "North Charleston, SC",
     "Lafayette, LA",
     "Arvada, CO",
     "Independence, MO",
     "Billings, MT",
     "Fairfield, CA",
     "Hartford, CT",
     "Ann Arbor, MI",
     "Broken Arrow, OK",
     "Berkeley, CA",
     "Cambridge, MA",
     "Richardson, TX",
     "Antioch, CA",
     "High Point, NC",
     "Clearwater, FL",
     "Pueblo, CO",
     "Pompano Beach, FL",
     "Springfield, IL",
     "Lowell, MA",
     "West Covina, CA",
     "Erie, PA",
     "Centennial, CO",
     "Norwalk, CA",
     "Carlsbad, CA",
     "Burbank, CA",
     "Westminster, CA",
     "Brockton, MA",
     "Visalia, CA",
     "Costa Mesa, CA",
     "Downey, CA",
     "Miami Gardens, FL",
     "El Cajon, CA",
     "San Mateo, CA",
     "Sandy Springs, GA",
     "North Hempstead, NY",
     "Lansing, MI",
     "Daly City, CA",
     "Rialto, CA",
     "El Monte, CA",
     "Elizabeth, NJ",
     "South Bend, IN",
     "Vacaville, CA",
     "West Jordan, UT",
     "Waterbury, CT",
     "Davenport, IA",
     "Roseville, CA",
     "Thornton, CO",
     "Alhambra, CA",
     "Beaumont, TX",
     "Lee's Summit, MO",
     "Allentown, PA",
     "Surprise, AZ",
     "Clarksville, TN",
     "Abilene, TX",
     "Round Rock, TX",
     "Amarillo, TX",
     "North Las Vegas, NV",
     "Lansing, MI",
     "Midland, TX",
     "Palmdale, CA",
     "Springfield, MO",
     "Pasadena, TX",
     "Macon, GA",
     "Pomona, CA",
     "Escondido, CA",
     "Denton, TX",
     "Waco, TX",
     "Joliet, IL",
     "McAllen, TX",
     "Bellevue, WA",
     "Rockford, IL",
     "Carrollton, TX",
     "Grand Prairie, TX",
     "Columbia, SC",
     "Miramar, FL",
     "Chula Vista, CA",
     "Sioux Falls, SD",
     "Port St. Lucie, FL",
     "North Charleston, SC",
     "Naperville, IL",
     "Overland Park, KS",
     "Santa Clarita, CA",
     "Cary, NC"
]
