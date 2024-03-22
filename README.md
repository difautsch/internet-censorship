# internet-censorship
data analysis at the intersection of cybersecurity and journalism
# instructions
Run censorship-rate to get percentage of blocked webpages. input = query_params, https://api.ooni.io/api/#operation/measurements.api.list_measurements

Run url-categorization to categorize a country's blocked content. input = list of country_codes. 
The excel files have raw data, some data cleaning formulas, and graphs. 

# analysis
The censorship rate is the percentage of blocked URLs. OONI maintains a global and country-specific list of URLs for testing. 
To get the content types I categorized the URLs using a keyword bank. 
The countries in the graph are the only countries who block more than 1% of URLs
