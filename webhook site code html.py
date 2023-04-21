<!DOCTYPE html>
<html>
  <head>
    <title>Webhook Sender</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Webhook Sender</a>
    </nav>
    
    <div class="container mt-5">
      <div class="row">
        <div class="col-md-6 offset-md-3">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Send Message to Webhook</h5>
              <form>
                <div class="form-group">
                  <label for="webhookName">Webhook Name:</label>
                  <input type="text" class="form-control" id="webhookName" name="webhookName" required>
                </div>
                <div class="form-group">
                  <label for="webhookURL">Webhook URL:</label>
                  <input type="url" class="form-control" id="webhookURL" name="webhookURL" required>
                </div>
                <div class="form-group">
                  <label for="message">Message:</label>
                  <textarea class="form-control" id="message" name="message" required></textarea>
                </div>
                <div class="form-group">
                  <label for="numWebhooks">Number of Webhooks:</label>
                  <input type="number" class="form-control" id="numWebhooks" name="numWebhooks" min="1" required>
                </div>
                <button type="button" class="btn btn-primary" onclick="sendMessages()">Send Messages</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <script>
      function sendMessages() {
        var webhookName = document.getElementById("webhookName").value;
        var webhookURL = document.getElementById("webhookURL").value;
        var message = document.getElementById("message").value;
        var numWebhooks = document.getElementById("numWebhooks").value;
        
        var data = JSON.stringify({
          "content": message,
          "username": webhookName
        });
        
        for (var i = 0; i < numWebhooks; i++) {
          $.ajax({
            url: webhookURL,
            type: "POST",
            data: data,
            contentType: "application/json",
            success: function(response) {
              console.log("Message sent successfully to webhook #" + i);
            },
            error: function(xhr, status, error) {
              console.log("Error sending message to webhook #" + i + ": " + error);
            }
          });
        }
        
        alert("Messages sent successfully!");
      }
    </script>
  </body>
</html>