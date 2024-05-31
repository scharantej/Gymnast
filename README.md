## **Acrobat: Online Shopping Cart with CRUD Operations**

### HTML Files

**1. home.html**
- This file serves as the landing page of the application.
- It displays a list of all products in the catalog along with options to add them to the cart.

**2. cart.html**
- This file manages the shopping cart.
- It shows the list of products currently in the cart, along with options to modify quantities, remove items, and checkout.

**3. checkout.html**
- This file collects necessary information for checkout, such as shipping and billing details.
- It allows users to complete their purchase and place the order.

**4. product_details.html**
- This file displays detailed information about a specific product.
- It includes product description, images, reviews, and an option to add the product to the cart.

**5. admin.html**
- This file provides an interface for administrators.
- It allows administrators to manage products, create discounts, and view order history.

### Routes

**1. @app.route('/')**
- Serves the home page (home.html).
- Displays the list of products.

**2. @app.route('/cart')**
- Serves the shopping cart page (cart.html).
- Allows users to manage their cart, checkout, and place orders.

**3. @app.route('/checkout')**
- Serves the checkout page (checkout.html).
- Collects necessary information for checkout and processes the order.

**4. @app.route('/product/<int:product_id>')**
- Serves the product details page (product_details.html).
- Displays detailed information about a specific product and allows users to add it to their cart.

**5. @app.route('/admin')**
- Serves the admin interface page (admin.html).
- Provides access to admin-only functionalities.

**6. CRUD API Routes:**
- A set of routes responsible for handling create, read, update, and delete operations for products and orders.
- Entities are created using POST requests.
- Entities are fetched using GET requests.
- Entities are updated using PUT requests.
- Entities are deleted using DELETE requests.

### Additional Notes

- The application uses a database to store products and orders.
- The CRUD API routes interact with the database to perform operations.
- User authentication and session management can be integrated into the application as needed.