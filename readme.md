# **Social Media App Backend**

A lightweight backend implementation for a social media application using Flask and MySQL. This project includes CRUD functionality for users, posts, comments, likes, and messages, with a clean and modular structure to simplify development and scalability.

---

## **Features**
- **User Management**: Create and retrieve user information.
- **Post Creation**: Users can create and view posts.
- **Commenting System**: Add and retrieve comments for posts.
- **Likes**: Users can like posts.
- **Direct Messaging**: Send and retrieve messages between users.
- **MySQL Integration**: Persistent storage for all entities.

---

## **Project Structure**
```
social_media/
├── app.py                 # Main Flask application
├── config.py              # MySQL database connection configuration
├── requirements.txt       # Python dependencies
├── db_setup.sql           # SQL script for database setup
└── README.md              # Project documentation
```

---

## **API Endpoints**

### **User Routes**
| Method | Endpoint         | Description          |
|--------|------------------|----------------------|
| GET    | `/users`         | Retrieve all users. |
| POST   | `/add_user`      | Add a new user.      |

### **Post Routes**
| Method | Endpoint         | Description          |
|--------|------------------|----------------------|
| GET    | `/posts`         | Retrieve all posts. |
| POST   | `/add_post`      | Add a new post.      |

### **Comment Routes**
| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | `/comments`      | Retrieve all comments.   |
| POST   | `/add_comment`   | Add a new comment.       |

### **Like Routes**
| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| GET    | `/likes`         | Retrieve all likes.  |
| POST   | `/add_like`      | Add a new like.       |

### **Message Routes**
| Method | Endpoint         | Description                 |
|--------|------------------|-----------------------------|
| GET    | `/messages`      | Retrieve all messages.      |
| POST   | `/send_message`  | Send a new message.         |

---

## **Technologies Used**
- **Programming Language**: Python
- **Framework**: Flask
- **Database**: MySQL
- **Dependencies**: Flask, MySQL Connector

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/social-media-backend.git
cd social-media-backend
```

### **2. Install Dependencies**
Make sure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```

### **3. Set Up the Database**
1. Install and configure MySQL on your machine.
2. Create the database and tables by running the `db_setup.sql` file:
   ```bash
   mysql -u your_username -p < db_setup.sql
   ```
3. Update the MySQL connection details in `config.py`.

### **4. Run the Application**
Start the Flask development server:
```bash
python app.py
```

### **5. Test the API**
Use tools like [Postman](https://www.postman.com/) or [Curl](https://curl.se/) to test the endpoints.

---

