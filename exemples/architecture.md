```md
Generate Java classes for purchase items and orders. 
## Order fields 
- List of line items to reference the order 
- The total amount of the order 
- The status of the order: Reveived Rejected and Accepted 

For each line item: 
- ItemId field that is associated to the item in the catalog 
- Item Price 
- Item Quantity 
## Example 
An order with Accepted Status could contain 2 line items:
- ItemId: 1, ItemPrice: 10, ItemQuantity: 5 
- ItemID: 2, ItemPrice: 19.99, ItemQuantity: 2 

The order TotalAmount is 89.98 
## Additional Rules 
- Maximum 10 line items per order
- Minimum 1 line item per order 
- Each line item must have a quantity greater than 0 
- Each item price must be greater than 0 

 Also generate a class diagram using Mermaid Markdown Think step by step, and revalidate answers
```

```yaml
openapi: 3.0.0
info:
  title: Order API
  version: 1.0.0
paths:
  /orders:
    get:
      summary: Returns a list of orders
      responses:
        '200':
          description: A JSON array of order objects
          content:
            application/json:
              schema: 
                type: array
                items: 
                  $ref: '#/components/schemas/Order'
    post:
      summary: Creates a new order
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Order'
      responses:
        '201':
          description: Order created
  /orders/{id}:
    get:
      summary: Returns a specific order
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: A single order object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
    put:
      summary: Updates a specific order
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Order'
      responses:
        '200':
          description: Order updated
    delete:
      summary: Deletes a specific order
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '204':
          description: Order deleted
components:
  schemas:
    Order:
      type: object
      properties:
        id:
          type: integer
        status:
          type: string
        totalAmount:
          type: number
        lineItems:
          type: array
          items: 
            $ref: '#/components/schemas/LineItem'
    LineItem:
      type: object
      properties:
        itemId:
          type: integer
        lineItemPrice:
          type: number
        lineItemQuantity:
          type: integer
```
