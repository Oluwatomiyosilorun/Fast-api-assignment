# FastAPI E-Commerce Challenge

## Overview
This repository presents the implementation of an E-Commerce API using FastAPI, featuring functionalities and endpoints as part of the assignment.

## Implemented Features
1. **Unique Username Validation**: Introduced a dependency to guarantee unique usernames when creating a customer.
2. **Customer Information Modification Endpoint**: Added an endpoint to edit customer details.
3. **Product Information Modification Endpoint**: Introduced an endpoint to modify product information.
4. **Order Status Attribute**: Included a status attribute in the Order entity with a default value of "pending".
5. **Order Checkout Endpoint**: Implemented an endpoint to transition the status of an order from "pending" to "completed".

## Project Structure
The project is organized as follows:
- `main.py`: Core FastAPI application setup and routing.
- `middleware.py`: Middleware handling logging and error management.
- `routers/`: Directory with router modules for different entities.
  - `customer.py`: Router module for customer-related endpoints.
  - `product.py`: Router module for product-related endpoints.
  - `order.py`: Router module for order-related endpoints.
- `schema/`: Directory with Pydantic models for data validation.
  - `customer.py`: Pydantic models for customers.
  - `product.py`: Pydantic models for products.
  - `order.py`: Pydantic models for orders.
- `services/`: Directory containing service modules for business logic.
  - `order.py`: Service module for order-related logic.
- `logger.py`: Module for logging configuration.
- `app.log`: Log file for application logs.
- `illustration.py`: Placeholder file for illustration purposes.

## Setup Instructions
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the FastAPI application using `uvicorn main:app --reload`.

## Usage
- Utilize the provided endpoints to interact with the E-Commerce API:
  - `/customers`: Perform CRUD operations for customers.
  - `/products`: Execute CRUD operations for products.
  - `/orders`: Conduct CRUD operations for orders.
  - `/orders/checkout/{order_id}`: Initiate the checkout process for an order.

