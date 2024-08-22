
### Background

In many areas of finance, the use of leverage is paramount to the success and viability of an investment strategy.  However,
investing with leverage is risky, and lenders who are providing the financing want to make sure they set appropriate parameters and constraints
for the borrower in an attempt to avoid an outcome where they lose their money.

In this project you are going to model out the allocation of the collateral for a hypothetical set of 3 leverage facilities for a fund that holds loans. **The end goal is to maximize return while minimizing expense.**


Located in the `data` directory you will find two files:
1. The `facilities.json` file describes the attributes and constraints of 3 example banks who are lending to us, the borrower.  The attributes have the following meanings:
   1. name = the name of the facility
   2. draw_fee = a one time fee as a percent of the amount borrowed each time we borrow from the facility.
   3. undrawn_fee = the annualized rate charged against any unused (or undrawn) portion of the facility (capacity - amount drawn)
   4. rate = the annualized rate charged against the used (or drawn) portfolio of the facility
   5. capacity = the maximum amount that can be borrowers (drawn) from the facility
   6. ltv = the required maximum "loan-to-value" that must be maintained at all times.  If the borrower does not maintain this level or better (lower) then they will be in default.  It's calculated as the (amount drawn) / (value of the collateral) = LTV.
   7. advance_rate = this is the amount of cash the lender will "advance" for a loan of a particular rating, A, B or C.  If the advance rate is 80%, then you can borrow up to 80% of the value of the loan that is pledged as collateral.  So if you pledge a $100K loan, you can borrow up to $80K.
   8. concentration = this is the MAX concentration that the entire collateral portfolio can have in any particular rating group, weighted by principal amount.  So if the collateral contains three loans of $100K each within ratings A, B, and C, their concentration is 33%, 33%, and 33% respectively and would be compared against these max concentration numbers.  Breaching these max concentration amounts is not allowed.

2. The `loans.json` file contains a list of 1000 randomly generated loans. While self-explanatory, the attributes are defined as:
   1. loan_id = the name of the loan
   2. rating = the rating, from A to C.  A being a loan with the most creditworthy borrower and C being a loan with the least creditworthy borrower.
   3. yield = the annualized amount the loan is expected to yield to its maturity
   4. principal = the amount of $$$ borrowed.
   

### Requirements
You will write a python application that takes as input the `facilities.json` and `loans.json` files and outputs a collateral report that identifies the following information:
   1. How much of each facility we have drawn and undrawn, if any.
   2. Which loans are pledged as collateral to which facilities, if any.  It is okay if loans aren't pledged as collateral, too.
   3. What the actual risk rating concentration (as a percent) is for each pool of collateral pledged to the facilities versus their stated maximums
   4. What the expected yield is on the portfolio, assuming yield is just a principal weighted average of the loan yields less the average fee/interest expense from the facilities.  Remember, not drawing down on a facility means that we pay the "undrawn fee".

Please check your solution into a github respository of your choosing and make it public so that the team can review your work.  Be prepared to answer questions about your solution during a group presentation.

