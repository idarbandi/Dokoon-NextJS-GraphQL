<div dir="ltr" >
   # Learn Microservices with the StackPay Project: From Idea to Implementation!

Hello to all dear developers!

My main goal in creating **StackPay** was to teach the architecture of microservices in the simplest possible way. This project is an online order registration system built with **two independent FastAPI services** so you can see the communication between services in practice. If you want to know how to break down large systems into smaller parts, read this article to the end!

---

## The Initial Idea: Two Independent Web Applications

When I started designing **StackPay**, the first question that came to my mind was:

**How can a complex system be divided into simple and independent parts?**

To answer this question, I designed two separate services:

1. **Product Service**: Managing product information (name, price, inventory).
2. **Order Service**: Registering and tracking orders.

Each service works independently, and even if one goes down, the other continues to function!

---

## Why ReactJS for Front-end?

For the front-end, I chose **ReactJS**, not Vue or NextJS. Here's why:

- **Large Community**: React is one of the most popular JavaScript libraries with thousands of free educational resources.
- **Flexibility**: You can use Redux for state management or CSS Modules for styling.
- **Compatibility with Microservices**: React easily works with various APIs and is great for multi-service projects.

---

## Why NoSQL and Why Redis?

### 1. Benefits of NoSQL for Microservices

- **Scalability**: Manage data without needing to change the structure.
- **High Speed**: Millisecond processing even for large volumes of data.

### 2. Why Redis?

- **In-memory Storage**: Access data at lightning speed!
- **Queue Management**: Use Redis CLI to manage messages between services.

### Setting Up Redis Cloud in Iran

To use **Redis Cloud** (Redis cloud management):

1. Go to [Redis Labs](https://redis.com/) and create an account.
2. Choose your desired plan (the free plan is suitable to start).
3. If you're in Iran and face restrictions, you can use local services like **AriaCloud** or **ParsPack** that offer similar services.

---

## Key Features of StackPay

- **Order Registration**: Select products and quantities with a few clicks.
- **Smart Error Handling**: If a user enters a negative number, the system warns them.
- **Responsive Design**: Suitable design for both mobile and desktop.

---

## Consumer Files and Their Importance

In microservices architecture, **consumers** play a vital role. These files are responsible for receiving and processing messages sent between services. For example, when a user registers a new order, the order service sends a message to Redis, and the product service's consumers receive this message to update the product inventory. This way, services work without direct dependency on each other, making the overall system more stable.

**Why Are Consumers Essential?**

- **Decoupling**: Services don't need to be directly connected.
- **Asynchronous Processing**: Even if one service goes down, messages remain in the queue and are processed later.
- **Scalability**: You can increase the number of consumers based on the workload.

---

## Installation and Setup

First, clone the repository and navigate to the project folder:

```bash
# Clone the repository
git clone https://github.com/idarbandi/StackPay.git
cd StackPay
```

Then install the front-end and back-end:

```bash
# Install front-end
cd frontend
npm install

# Install back-end
cd ../backend
pip install -r requirements.txt
```

To run the services, execute the following commands:

```bash
# Run front-end
cd ../frontend
npm start

# Run back-end
cd ../backend
uvicorn main:app --reload
```

---

## How to Test Payment and Inventory Services

After installing and setting up the services, you can test both the payment and inventory applications using the following commands.

### Testing the Inventory Service

```bash
# Run the product service
cd inventory_service
uvicorn main:app --reload --port 8000
```

```bash
# Get the list of products
curl -X GET http://localhost:8000/products

# Add a new product
curl -X POST http://localhost:8000/products \
-H "Content-Type: application/json" \
-d '{"name": "Laptop", "price": 1500, "quantity": 10}'
```

### Testing the Order Service

```bash
# Run the order service
cd ../order_service
uvicorn main:app --reload --port 8001
```

```bash
# Register a new order
curl -X POST http://localhost:8001/orders \
-H "Content-Type: application/json" \
-d '{"product_id": 1, "quantity": 2}'

# Get the list of orders
curl -X GET http://localhost:8001/orders
```

**Notes:**

- By running the product service on port 8000 and the order service on port 8001, you can test each service independently.
- In the above requests, appropriate HTTP methods are used (**GET** to retrieve data and **POST** to create new data).
- Be sure to align product IDs and values with the data existing in your system.

---

### Important Note About Testing Services

To ensure that the communication between services works correctly, you can test the following scenario:

1. **Create a new product** in the product service:

   ```bash
   curl -X POST http://localhost:8000/products \
   -H "Content-Type: application/json" \
   -d '{"name": "Smartphone", "price": 800, "quantity": 50}'
   ```

2. **Register a new order** for the same product in the order service:

   ```bash
   curl -X POST http://localhost:8001/orders \
   -H "Content-Type: application/json" \
   -d '{"product_id": 1, "quantity": 5}'
   ```

3. **Check the product inventory** after registering the order to see if the inventory has decreased correctly:

   ```bash
   curl -X GET http://localhost:8000/products/1
   ```

**Note:** If everything is configured correctly, the product inventory should have decreased by the order quantity. This shows that the services are communicating well with each other, and messages are being transferred between them via Redis.

---

### Comments and Docstrings in Persian in the Code

If you look at the project's code, you'll notice that I've used **readable comments and docstrings in Persian** for all Python and JavaScript files. These explanations help you to:

- **Better understand the logic behind each function and class.**
- **Learn how services communicate with each other.**
- **Understand complex concepts in simple language.**

**Example of Persian Docstrings in Python:**

```python
class Product(BaseModel):
    """
    Class representing a product that holds product information.
    Fields:
    - name: Name of the product
    - price: Price of the product
    - quantity: Inventory of the product in stock
    """
    name: str
    price: float
    quantity: int
```

---

## Using Swagger UI to Test APIs

One of the powerful tools for testing and documenting APIs is **Swagger UI**. With Swagger UI, you can easily view and test all your endpoints without needing tools like Postman.

### Benefits of Using Swagger UI

- **User-friendly Interface**: There's no need to manually write requests; everything is done through a graphical interface.
- **Automatic Documentation**: Descriptions of endpoints, parameters, and responses are automatically generated.
- **Quick Testing**: Ability to send requests and see responses instantly.

### Adding Swagger UI to the StackPay Project

Since we're using **FastAPI**, Swagger UI is embedded by default. To access Swagger UI, after running the services, visit the following addresses:

- **Product Service**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Order Service**: [http://localhost:8001/docs](http://localhost:8001/docs)

By opening these addresses in your browser, you can view and test all the endpoints related to each service.

### Using Swagger UI in Django Projects

If you want to add **Swagger UI** to your **Django** applications, you can use the **drf-yasg** package. Follow these steps:

1. **Install the drf-yasg package**:

   ```bash
   pip install drf-yasg
   ```

2. **Add it to `INSTALLED_APPS`** in your `settings.py` file:

   ```python
   INSTALLED_APPS = [
       # ...
       'rest_framework',
       'drf_yasg',
       # ...
   ]
   ```

3. **Define Swagger routes in your `urls.py` file**:

   ```python
   from django.urls import path, re_path
   from rest_framework import permissions
   from drf_yasg.views import get_schema_view
   from drf_yasg import openapi

   schema_view = get_schema_view(
       openapi.Info(
           title="API Documentation",
           default_version='v1',
           description="Test Description",
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )

   urlpatterns = [
       # ...
       re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
       path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
       path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
       # ...
   ]
   ```

4. **Access Swagger UI**:

   After running the Django server, you can visit [http://localhost:8000/swagger/](http://localhost:8000/swagger/) to see Swagger UI.

**Note:** Be sure to use **Django REST Framework** to build your APIs so that Swagger can recognize them.

---

## Invitation to Collaborate and Expand the Project

I invite you to help improve and expand **StackPay** by participating in its development. Your ideas, suggestions, and feedback can lead to enhancing the quality of this project.

- **Report Bugs**: If you encounter any issues, raise them in the GitHub Issues section.
- **Add New Features**: You can submit your pull requests to add new capabilities.
- **Translation and Documentation**: Help improve documentation and translate it into other languages.

---

### Further Learning Resources

If you're interested in learning more about microservices, FastAPI, and Redis, I recommend the following resources:

- **Official FastAPI Documentation**: [FastAPI Documentation](https://fastapi.tiangolo.com/)
- **Redis Tutorials**: [Redis Tutorials](https://redis.io/documentation)
- **Microservices Concepts**: Articles and books related to microservices architecture.
- **Using Swagger with Django**: [drf-yasg Documentation](https://drf-yasg.readthedocs.io/en/stable/readme.html)

---

**In conclusion,** I hope this project and its explanations have been helpful to you. If you have any questions or need further guidance, feel free to contact me.

Best wishes! 🌟

**Contact Me:**

Email: darbandidr99@gmail.com

GitHub: [idarbandi](https://github.com/idarbandi)

---

If you're interested in deeper learning, I recommend following the project's code carefully. In all Python and JavaScript files, I've used meaningful and deep comments and docstrings in Persian. These explanations are written in-depth to give you a better understanding of the program logic and microservices structure.

By reviewing the code, you can thoroughly learn how services communicate, data management, and system optimization. If you have any questions or need further guidance, be sure to get in touch.

Best of luck! 🌟

---

For Iranians interested in the Persian version of this article, you can read it here: [میکروسرویس‌ها را با پروژه StackPay یاد بگیرید: از ایده تا اجرا!](https://virgool.io/@darbandidr99/میکروسرویس-ها-را-با-پروژه-stackpay-یاد-بگیرید-از-ایده-تا-اجرا-lmntajbetsno)
</div>