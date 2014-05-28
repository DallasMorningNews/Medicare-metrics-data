Medicare provider metrics data
==============================

This is _The Dallas Morning News'_ re-release of 2012 Medicare Part B provider billing data with procedure-specific statistical comparators. 

With these data, you too can find statistical outliers in your state in terms of [procedure use rates](http://www.dallasnews.com/investigations/20140524-examining-the-cost-of-too-much-care.ece) [per Medicare patient](http://res.dallasnews.com/interactives/2014_May/medicare-viz/)!

The raw data is broken into compressed files for each state or territory. Each is a comma-delimited file.* 

Each row in each data table represents a provider's billings for a particular medical procedure or service in 2012, just like in Medicare's original release.

For general info on the data and a description of the provider specific fields in each table, have a look at Medicare's information [here](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Physician-and-Other-Supplier.html).


Additional fields in these tables were calculated by _The News_:

- **total_payments**  

>>Total payments made to the provider by Medicare for the service. Calculated as the product of the average Medicare payment times the number of services billed.

- **services_per_bene**

>>The rate which is the number of services administered by the provider per Medicare patient who received the service.  

- **national_avg_serv_per_bene**

>>The national average services per beneficiary rate among all other providers within the provider's specialty who also administered the service in 2012.

- **national_stddev_serv_per_bene**

>>The national (population) standard deviation of the services per beneficiary rate among all other providers within the provider's specialty who also administered the service in 2012.

- **stddev_above_avg**

>>The number of standard deviations a provider's rate is above the national average. For _The News'_ analysis, we looked at those providers who were more than 3 standard deviations above the national average.

- **variation_coefficient_serv_per_bene**

>>The coefficient of variation is a normalized measure of the variability of a dataset. It's calculated by taking the standard deviation divided by the mean. We used it to compare procedures with high variability to those with low variability in a provider's practice.

- **num_of_providers**

>>The number of providers included in the average to which the provider is compared to. We looked at procedures that included more than 100 providers in the comparison for our analysis.

- **national_rank**

>>How this provider's per-patient rate ranks nationally. We focused on providers in Texas whose rate ranked first nationwide.



>_*createTable.sql can be used to create the table schema in PostgreSQL databases._