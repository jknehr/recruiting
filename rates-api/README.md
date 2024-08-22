### Background
In this project you are going to create a Python service that calculates the projected interest rate of a floating rate loan and delivers the result via a REST API.

A floating rate loan is a loan where the interest rate changes each month based on the prevailing market rates and future expectations of those rates.  The final interest rate that is used to calculate the interest due in a particular month is equal to the reference rate's projected value + a fixed spread.  For example, if the forward rates for the next 3 months are 1.5%, 1.75%, and 2.00% respectively, and the spread on the loan is 2.00%, then the final interest rate that is used to calculate the interest due is 3.50%, 3.75%, and 4.00% for each of the next 3 months.  Additionally, many loans have a minimum and maximum value that the rate can be in any month.  This is to ensure that if the reference rate gets too small or too large that the final rate doesn't go outside a pre-agreed range. These mins and maxes are called rate floors and ceilings, respectively.

Please spend no more than 4 hours on this.  The intent isn't to build a production ready application but to showcase your skill with a small toy project.  Anything submitted that isn't part of the requirements below will also be considered as part of our assessment.


### Requirements
1. Since interest rates changes daily, you first need to source the current rates.  [Pensford](https://www.pensford.com/resources/forward-curve) offers calculated rates on a daily basis on their website and in a corresponding attachment.  So does [Chatham Financial](https://www.chathamfinancial.com/technology/us-forward-curves). You shall write a small ETL script in python that extracts the 1-Month SOFR forward rates from one of these websites (you choose) and stores them in a data store of your choosing (e.g. SQLlite, etc).  You may use any libraries you want.
2. Next you are to create a RESTful endpoint (e.g. with [FastAPI](https://fastapi.tiangolo.com/)) that when you POST a payload with loan details, it calculates what the forward applicable interest rate will be for the provided loan taking into consideration the details of the loan and the latest rates that you stored from Pensford or Chatham.  The loan payload will look as follows:
`{
"maturity_date": "2022-02-01",
"reference_rate": "SOFR",
"rate_floor": 0.02,
"rate_ceiling": 0.10,
"rate_spread": 0.02
}`.  The returned rate curve should not extend beyond the maturity date of the loan and can make reference to either of the LIBOR or SOFR rate curves.  The returned payload should be a list of objects that includes the date and rate values, such as `[{"date": "2022-01-01", "rate":0.03}, {"date":"2022-02-01", "rate":0.0325}, ...]`

### Deliverables
1. There are two components to the solution and therefore the solution should be delivered in two parts.  The first part is the rates ETL job, which should be runnable on its own and write the appropriate data to the data store.  The second part should be a standalone service that exposes a REST endpoint to perform the calculation.  Bonus: Dockersize the API service such that it could be deployed into a cloud environment.
2. Push the full solution into a GitHub repository of your choosing.  Make sure the repository visibility is set to public.
3. Give a small write-up in a root-level Readme file that describes how to run the solution. Include how much time you spent.  Additionally, include a list of areas for improvement or further consideration if you were going to take this project and make it production ready.
4. Be prepared to discuss your solution and present it to the team.
