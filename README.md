project structure
.
├── README.md
├── app -> main code
│ ├── **init**.py
│ └── main -> modules yang akan kita gunakan
│ ├── **init**.py
│ ├── controller -> code yang akan kita gunakan untuk menerima FLASK Request
│ ├── model -> code yang akan merepresentasikan model python ke model database
│ ├── repository -> code yang kita gunakan untuk query / mendapatkan data dari database
│ └── util -> code yang akan membantu kita (validation, dto)
└── run.py

# Migration

```
flask --app run db init
flask --app run db migrate --message "add user model"
flask --app run db upgrade
```
