| Method | Endpoint            | Purpose                                  |
| ------ | ------------------- | ---------------------------------------- |
| POST   | `/predict`          | Upload an image and receive a prediction |
| GET    | `/predictions`      | View prediction history                  |
| GET    | `/predictions/{id}` | View a specific prediction               |
| DELETE | `/predictions/{id}` | Delete a prediction                      |
| POST   | `/feedback/{id}`    | Correct a prediction                     |
| GET    | `/health`           | Health check for deployment              |
| GET    | `/logout`           | Log out                                  |
| GET    | `/me`               | Get user info                            |