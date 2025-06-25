# Floating Rate Loan Interest API – Take-Home Project

## Overview

In this project, you’ll build a small Python service that calculates the projected interest rate for a floating rate loan and exposes the result via a REST API.

A floating rate loan is one where the interest rate adjusts periodically, typically monthly, based on market expectations of a reference rate (e.g., SOFR or LIBOR). The final interest rate for each period is calculated as:

```
final_rate = reference_rate + spread
```

However, many loans include contractual rate **floors** (minimum) and **ceilings** (maximum), which limit the final rate after the spread is applied.

For example, if the next three months of 1-month SOFR forward rates are:
- 1.50%, 1.75%, and 2.00%

And the loan spread is 2.00%, the raw calculated rates are:
- 3.50%, 3.75%, and 4.00%

If the floor is 3.00% and the ceiling is 3.60%, the final applicable rates would be:
- 3.50%, 3.60%, and 3.60%

This project is not expected to be production-grade, but should reflect your skills and approach to solving technical problems.

---

## Timebox

Please spend no more than **4 hours** on this project.

---

## Requirements

Your solution should be delivered in two parts:

### Part 1: Rate Data Retrieval

- Write a Python script that downloads and extracts **1-month forward rates** for **SOFR** from a public source such as **[Pensford](https://www.pensford.com/resources/forward-curve)** or **[Chatham Financial](https://www.chathamfinancial.com/technology/us-forward-curves)**.
- Use a structured source format (e.g. downloadable CSV or Excel files).
- Store the parsed rates in a persistent store of your choice (e.g. SQLite, PostgreSQL, etc.).
- In your README, document:
  - Which data source you chose and why.
  - Any data transformation decisions made.

### Part 2: REST API

- Create a RESTful service using a framework like **[FastAPI](https://fastapi.tiangolo.com/)**.
- The service should expose a `POST` endpoint at `/loan-rate-curve`.
- This endpoint should accept a JSON payload with loan details:

```json
{
  "maturity_date": "2025-12-01",
  "reference_rate": "SOFR",
  "rate_floor": 0.02,
  "rate_ceiling": 0.10,
  "rate_spread": 0.02
}
```

- The response should be a list of projected rates, one per month up to (but not exceeding) the maturity date. For example:

```json
[
  {"date": "2024-07-01", "rate": 0.035},
  {"date": "2024-08-01", "rate": 0.0375},
  ...
]
```

- Use the latest available forward rates stored from your ETL script.
- Apply rate floors and ceilings after adding the spread to the base rate.

---

## Bonus

- Dockerize the API so it can be run in a local containerized environment.
- Implement simple retry logic or backoff in your data download script.

---

## Deliverables

- A public GitHub repository containing:
  - Your ETL script
  - Your API implementation
  - A README file (this one is a good starting point)
- Please also include:
  - A short write-up in your README explaining how you approached the rate logic, what assumptions you made, and any trade-offs you considered.
  - Instructions to run the solution locally
  - Approximate time spent
  - Notes on what you would improve if given more time

---

## Evaluation

We’re interested in:

- Clear, maintainable code
- Sensible design choices
- Effective use of Python and RESTful practices
- Realistic modeling of rate logic and constraints

Be prepared to walk us through your code in a short follow-up discussion.

---

Thanks for taking the time to complete this exercise — we look forward to reviewing your solution!
