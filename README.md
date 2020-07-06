# crud-products-django

#### Endpoints for Products

Method |  Endpoint  | Description
-------|------------|------------
POST | **/api/product/** | Create an product on database
GET | **/api/product/** | Return a list containing all products information
GET | **/api/product/?name=<name_to_search>** | Search for product whose name contains the "name_to_search" string
GET | **/api/product/?price=<price_to_search>** | Search for product whose price contains the "price_to_search" string
GET | **/api/product/<**id**>/** | Retrieve information of the product with the specified id
PATCH, PUT | **/api/product/<**id**>/** | Update the product information with the specified id
DELETE |  **/api/product/<**id**>/** | Delete the product with the specified id

Payload for POST/PUT:
```
{
    "name": // name of the product,
    "price": // price of the product
}
```
